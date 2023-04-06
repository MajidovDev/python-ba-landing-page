from django.shortcuts import render, redirect
from .models import Course, myUserModel
from .forms import UserForm
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def landing_page(request):
    courses = Course.objects.all().order_by('-created_at')
    course = courses[0]
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # if phone[0] != '+':
        #     print('hey')
        #     phone = '+'+phone
        #     print(phone)
        if message == '':
            message = "Xabar qoldirmadi!"
        text = f"Application:" \
               f"\nFull Name: {full_name}" \
               f"\nPhone Number: +{phone} " \
               f"\nCourse: {course.title}" \
               f"\nMessage: {message}"
        bot_token = "6246157864:AAEdsxCfnmABIVHS1Au3BBr8DFCaG7QJzi0"
        chat_id = "1261374933"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
        r = requests.get(url)

    context = {
        "course":course,
        "form": UserForm()
    }

    return render(request, 'landing_page.html', context)

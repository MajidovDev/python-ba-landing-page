from django.contrib import admin
from .models import Student, Course, CourseReview, ModuleCourse, IntroductionInfo, myUserModel

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseReview)
admin.site.register(IntroductionInfo)
admin.site.register(ModuleCourse)
admin.site.register(myUserModel)
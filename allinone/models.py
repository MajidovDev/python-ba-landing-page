from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    title = models.CharField(max_length=150)  # VARCHAR()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_picture = models.ImageField(default="default_cover.png")

    def __str__(self):
        return self.title


class IntroductionInfo(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    body = models.TextField()
    picture = models.ImageField(null=True, default='default-picture.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(AbstractUser):
    profile_picture = models.ImageField(default="default_profile_pic.png")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)


class CourseReview(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.TextField()
    starts_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.starts_given} stars for {self.course.title} by {self.user.first_name} {self.user.last_name}'


class ModuleCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.course.title} - module {self.id}"


class myUserModel(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} {self.phone}"

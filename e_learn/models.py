import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)


class Institution(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Subscription(models.Model):
    currency_choices = [
        ('CAD', 'CANADA'),
        ('USD', 'AMERICA')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    currency = models.CharField(choices=currency_choices, default='CAD', max_length=3)
    is_basic = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)


class UserInstitutionRelation(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)


class Course(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(default=None, null=True, blank=True)
    # Institution that created the course
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)


class UserCourseRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    final_grade = models.IntegerField(blank=True, null=True)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)


def get_file_path_notes(instance, filename):
    return "notes/" + str(instance.course.id) + "/" + str(filename)


class Notes(models.Model):
    name = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    notes_doc = models.FileField(upload_to=get_file_path_notes)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]


def get_file_path_assignment(instance, filename):
    return "assignment/" + str(instance.course.id) + "/" + str(filename)


class Assignment(models.Model):
    name = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True)
    created_on = models.DateField(auto_now_add=True)
    assignment_doc = models.FileField(upload_to=get_file_path_assignment)
    grade_points = models.IntegerField(null=True)

    class Meta:
        ordering = ["created_on"]

def get_file_path_assignment_submission(instance, filename):
    return "submission/" + str(instance.assignment.course.id) + "/" + str(filename)

class AssignmentGrades(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_status = models.BooleanField(default=False)
    assignment_doc = models.FileField(upload_to=get_file_path_assignment_submission, null=True)

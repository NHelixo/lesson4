from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name="teacher", null=True, blank=True)


class Class(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)

    class_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name="student", null=True, blank=True)


class Schedule(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True, blank=True)
    weekday = models.CharField(max_length=10, null=True)
    lesson_num = models.PositiveIntegerField(null=True)


class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, blank=True)

from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    related = models.ForeignKey(Subject, related_name="teacher", on_delete=models.DO_NOTHING)


class Class(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)

    related = models.ForeignKey(Class, related_name="student", on_delete=models.DO_NOTHING)

from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)


class Class(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)

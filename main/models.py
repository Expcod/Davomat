from django.db import models

class Staff():
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    work = models.CharField(max_length=255)


class Attendance():
    time = models.DateTimeField()

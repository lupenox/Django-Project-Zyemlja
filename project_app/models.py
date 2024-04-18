from django.db import models

#needs to be edited later to reflect our program for database purposes
class Patient:
    first_name = models.charField(max_length=50)
    age = models.IntegerField
    Physician = models.ForeignKey(Physician, on_delete=models, null=true)

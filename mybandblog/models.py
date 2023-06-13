from django.db import models

class Member(models.Model):
    name_member = models.CharField(max_length=200)
    age_member = models.IntegerField()
    id = models.IntegerField(primary_key=True)



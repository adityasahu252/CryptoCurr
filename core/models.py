from django.db import models

class Currency_Details(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    price=models.CharField(max_length=200)
    change=models.CharField(max_length=200)
    percent_change=models.TextField(max_length=150)


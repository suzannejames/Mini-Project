from django.db import models

class Languages_offered(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')

class Langs(models.Model):
    name=models.CharField(max_length=250)
    name1=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)

class Teachers(models.Model):
    name= models.CharField(max_length=250)
    lang= models.CharField(max_length=250)
    prof= models.CharField(max_length=250)
    rating= models.CharField(max_length=250)


class user_Registration(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=100)
    lang=models.CharField(max_length=100)
    email=models.EmailField()
    phone= models.CharField(max_length=10)
    password= models.CharField(max_length=100)
    password1= models.CharField(max_length=100)


class tutor_Registration(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=100)
    lang=models.CharField(max_length=100)
    email=models.EmailField()
    phone= models.CharField(max_length=10)
    password= models.CharField(max_length=100)
    password1= models.CharField(max_length=100)
    interview = models.BooleanField(default=False)

class Contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()

class SC(models.Model):
    day=models.CharField(max_length=7)
    time=models.TimeField()
    note=models.TextField()

    def __str__(self):
        return self.name



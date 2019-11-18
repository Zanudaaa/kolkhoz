from django.db import models

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_text = models.TextField()
    news_date = models.DateTimeField()

class Contacts(models.Model):
    contacts_name = models.CharField(max_length=50)
    contacts_photo = models.ImageField(upload_to='contacts_images')
    contacts_text = models.TextField()

class Faq(models.Model):
    faq_title = models.CharField(max_length=50)
    faq_describe = models.TextField()
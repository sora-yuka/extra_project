from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string

User = get_user_model()

class Category(models.Model):
    title =  models.SlugField(unique=True, primary_key=True) #? Slugfield - ограничивает допустимые символы
    
    
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    
    # def save(self, *args,) -> None:
    #     print("OLOLOLOLO")
    #     return super().save(*args)
    
@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    # print(sender)
    # print(instance)
    # print(created)
    # print(kwargs)
    
    # if created:
    #     instance.price += 100
    #     instance.save(update_fields=["price"])
        
        send_mail(
            "Greatings!!",
            "",
            "sabyrkulov.nurmuhammed@gmail.com",
            [User.email],
            html_message=render_to_string("send_mail.html", {"name": instance.title, "price": instance.price})
        )
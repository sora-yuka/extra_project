from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title =  models.SlugField(unique=True, primary_key=True) #? Slugfield - ограничивает допустимые символы
    
    
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    
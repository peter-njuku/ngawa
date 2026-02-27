from django.db import models
from django.utils.text import slugify

# Create your models here.
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    submitted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.name} ({self.email}) -- {self.submitted_at.strftime('%Y-%m-%d %H-%M')}"
    
class Products(models.Model):
    CATEGORY_CHOICES=[
        ('laptops','Laptops'),
        ('desktops','Desktops'),
        ('printers','Printers'),
        ('accessories','Accessories')
    ]

    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    slug=models.SlugField(unique=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.name)
    

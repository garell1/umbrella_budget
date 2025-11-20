from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return f"{self.name} - {self.category}"
    

class Expense(modsels.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', on_delete=models.CASCADE)
    provide_amount = models.DecimalField(max_digits=10, decimal_places=2)
    real_amount = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(max_length=200)
    month = models.DateField()
    
    def __str__(self):
        return f"{self.month} {self.category}: {self.subcategory} {self.provide_amount} {self.real_amount}"
    

class Income(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', on_delete=models.CASCADE)
    provide_amount = models.DecimalField(max_digits=10, decimal_places=2)
    real_amount = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(max_length=200)
    month = models.DateField()
    
    def __str__(self):
        return f"{self.month, self.category, self.subcategory, self.provide_amount, self.real_amount}"
    
    
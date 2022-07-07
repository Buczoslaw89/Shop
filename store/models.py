from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.core.validators import RegexValidator
from . forms import forms, CreateUserForm
from django.utils.html import mark_safe


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural='1. Klienci'

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Biżuteria złota', 'Biżuteria złota'),
        ('Biżuteria srebrna', 'Biżuteria srebrna'),
        ('Biżuteria stalowa', 'Biżuteria stalowa'),
        ('Zegarki', 'Zegarki'), ('Monety', 'Monety'),
        ('Upominki', 'Upominki'), ('Obrączki', 'Obrączki'),
        ('Akcesoria', 'Akcesoria'),
                )
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    is_feature = models.BooleanField(default=False, null=True, blank=False)

    class Meta:
        verbose_name_plural='2. Produkty'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    STATUS = (
    ('Przyjęte', 'Przyjęte'),
    ('Realizowanie', 'Realizowanie'),
    ('Zakończone', 'Zakończone'), 
            )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    class Meta:
        verbose_name_plural='3. Zamówienia'

    def __str__(self):
        return str(self.transaction_id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
                return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='4. Przedmioty z zamówień'

    @property
    def get_total(self):
        total = (self.product.price * self.quantity)
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='5. Adresy dostaw'

    def __str__(self):
        return self.address

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    pin = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Courier(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20)


class Brand(models.Model):
    brand = models.CharField(max_length=50)
    status = models.CharField(max_length=20)


class Cabin(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    material = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Cables(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Display(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    resolution = models.CharField(max_length=200)
    panel = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Hdd(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    speed = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Keyboard(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Motherboard(models.Model):
    name = models.CharField(max_length=50)
    socket = models.CharField(max_length=50)
    chipset = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Mouse(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Processor(models.Model):
    name = models.CharField(max_length=50)
    cache = models.CharField(max_length=50)
    speed = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Ram(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    speed = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Smps(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    wattage = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rate = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products', null=True)


class Assemble(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    cables = models.ForeignKey(Cables, on_delete=models.CASCADE)
    hdd = models.ForeignKey(Hdd, on_delete=models.CASCADE)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    smps = models.ForeignKey(Smps, on_delete=models.CASCADE)

    total = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    orderDate = models.DateField(auto_now_add=True)


class Assign(models.Model):
    assemble = models.ForeignKey(Assemble, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)

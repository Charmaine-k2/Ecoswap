from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, nickname, full_name, address, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone_number=phone_number,
            nickname=nickname,
            full_name=full_name,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, nickname, full_name, address, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            username=username,
            email=email,
            phone_number=phone_number,
            nickname=nickname,
            full_name=full_name,
            address=address,
            password=password,
            **extra_fields
        )
class CustomUser(AbstractUser):
    theme = models.CharField(max_length=20, default='light')
    address = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    alternative_phone_number = models.CharField(max_length=15, blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Item(models.Model):
    TRADE = 'trade'
    DONATE = 'donate'
    CATEGORY_CHOICES = [
        (DONATE, 'Donation'),
        (TRADE, 'Trade'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    image = models.ImageField(upload_to='items_images/', blank=True, null=True, default='images/default-image.png')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    condition = models.CharField(max_length=50, default='Good')  # e.g., New, Good, Fair, Poor
    status = models.CharField(max_length=50, default='Available')  # e.g., Available, Not Available
    item_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Trade(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    offered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trades_offered')
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_chats', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_chats', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
   


    def __str__(self):
        return f'{self.sender} to {self.receiver} at {self.timestamp}'


class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Query from {self.name}: {self.subject}"

class Delivery(models.Model):
    item = models.OneToOneField('Item', on_delete=models.CASCADE, null=True, blank=True)
    delivery_address = models.TextField()
    location = models.CharField(max_length=255)  # Optional: could be derived from address
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    driver = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    delivery_items = models.TextField()
    pickup_items = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')  # e.g., Pending, In Transit, Delivered                                                                                         

    def __str__(self):
        return f'Delivery for {self.item.name} on {self.delivery_date} at {self.delivery_time}'


class DonationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('scheduled', 'Scheduled'),
        ('rejected', 'Rejected'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.TextField()
    organization = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    scheduled_date = models.DateField(null=True, blank=True)
    scheduled_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.item.name} ({self.status})"

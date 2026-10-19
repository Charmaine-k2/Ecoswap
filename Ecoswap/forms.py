from django import forms
from .models import Item, Message
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

from .models import Query

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category','condition','image']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    alternative_phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'phone_number', 'alternative_phone_number', 'address', 'gender', 'password1', 'password2')




class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['name', 'email', 'subject', 'message']
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from .models import Post,Group
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2','profile')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'profile') 
        exclude = ('password',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # パスワードフィールドをフォームから削除
        self.fields.pop('password', None)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image1']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image1']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'text', 'category','share']

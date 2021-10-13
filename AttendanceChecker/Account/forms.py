from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

def randomFriendCode():
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        if CustomUser.objects.filter(friendCode = password).exists():
            continue
        else:
            return password

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {"first_name","last_name",'username','email','is_teacher'}
        def save(self, commit = True):
            user = super(CustomUserCreationForm, self).save(commit = False)
            user.email = self.cleaned_data['email']
            user.friendCode = randomFriendCode()
            if user.is_teacher == True:
                user.is_student = False
            else:
                user.is_student = True
            if commit:
                user.save()
            return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = {'username','email'}


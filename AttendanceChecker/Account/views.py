from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.
def SignUpView(request):
    if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
        return render(request, "registration/signup.html", {"form":form})

def AccountPageView(request):
    currentUser = request.user
    if currentUser.is_teacher == True:
        return render(request, "Account/accountpageteacher.html")
    else:
        return render(request, "Account/accountpage.html")

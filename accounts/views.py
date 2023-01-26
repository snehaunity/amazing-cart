from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from faker import Faker
import random

faker = Faker()

# def add_data_to_db(request):
#     shape = ['Oval', 'Shperical', 'Parabolic', 'Circle', 'Rectagular', 'Cone', 'Cylinder']
#     products = [Product(shape=random.choice(shape), size=faker.random.randint(1,50), location=faker.city(), price=faker.random.randint(100,1000)) for i in range(100000)]
#     Product.objects.bulk_create(products)
#     return HttpResponse("DATA INSERTED")


def logout_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('logout')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

@logout_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@logout_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def view_users(request):
    users = User.objects.select_related('userprofile').all()
    return render(request, "user.html", context={'users':users})

def update_profile(request, id):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        address = request.POST.get("address")
        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        user_profile = user.userprofile
        user_profile.age = age
        user_profile.address = address
        user_profile.save()
        return redirect("view-users")
    else:
        return redirect("view-users")



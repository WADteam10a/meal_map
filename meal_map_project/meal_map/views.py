from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Restaurant
from .forms import UserForm, UserProfileForm

# This view is used to take all the restaurant objects in the database and
# show it in a list formate
class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurant_list.html'  # Still need to adjust path
    context_object_name = 'restaurants'

# This view will get each the description of each restaurant object
    # DetailView will show all the information about the object
class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurants/restaurant_detail.html'  # Adjust path Later
    context_object_name = 'restaurant'
    
    
# Just the base html template, so i can see how it looks when im working on it - Luke
def base(request):
    
    response = render(request, 'meal_map/base.html')
    return response


def login(request):
    response = render(request, 'meal_map/login.html')
    return response

@login_required
def logout(request):
    return HttpResponse("Logout to be implemented")

def homepage(request):
    response = render(request, 'meal_map/homepage.html')
    return response

def my_account(request):
    response = render(request, 'meal_map/account.html')
    return response


def add_restaurant(request):
    response = render(request, 'meal_map/add_restaurant.html')
    return response

def my_reviews(request):
    response = render(request, 'meal_map/my_reviews.html')
    return response

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
        'meal_map/register.html',
         context = {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})

def restaurant(request):
    response = render(request, 'meal_map/restaurant.html')
    return response
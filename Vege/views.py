from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Receipe

# Register new user
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("recipes")

    return render(request, "register.html")


# Login page
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("recipes")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")


# Logout
def logout_user(request):
    logout(request)
    return redirect("login")


# Only logged‑in users can open this page
@login_required(login_url="login")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect("recipes")

    all_recipes = Receipe.objects.all()
    return render(request, "recipes.html", {"recipes": all_recipes})
@login_required(login_url='login')
def update_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)

    if request.method == "POST":
        recipe.receipe_name = request.POST.get('receipe_name')
        recipe.receipe_description = request.POST.get('receipe_description')

        if request.FILES.get('receipe_image'):
            recipe.receipe_image = request.FILES.get('receipe_image')

        recipe.save()
        return redirect('recipes')

    return render(request, 'update_recipe.html', {'recipe': recipe})


@login_required(login_url='login')
def delete_recipe(request, id):
    recipe = get_object_or_404(Receipe, id=id)
    recipe.delete()
    return redirect('recipes')

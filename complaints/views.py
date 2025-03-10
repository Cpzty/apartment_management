from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # Import the new form

from .models import Complaint
from .forms import ComplaintForm

# Home Page View
def home(request):
    return render(request, 'home.html')

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Register View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')  # Redirect to login after successful registration
        else:
            messages.error(request, "Please correct the error(s) below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES) #handle images
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user  # Assign the logged-in user
            complaint.save()
            return redirect('complaint_list')  # Redirect after submission
    else:
        form = ComplaintForm()
    
    return render(request, 'complaints/submit_complaint.html', {'form': form})

@login_required
def complaint_list(request):
    complaints = Complaint.objects.filter(user=request.user)  # Only show user complaints
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})



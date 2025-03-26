from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import ProfileForm, RegistrationForm
from .models import Event, Profile

# Function-based views for user-related pages

def home(request):
    # Assuming you want to display all events on the home page
    events = Event.objects.all()
    return render(request, 'users/home.html', {'events': events})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_update(request):
    # Try to get the profile, or create one if it doesn't exist
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_update.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# Class-based views for Event CRUD operations

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'users/event_form.html'
    success_url = reverse_lazy('home')  # Redirect to home after creation
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Event created successfully!")
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = Event
    template_name = 'users/event_detail.html'

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'users/event_form.html'
    success_url = reverse_lazy('home')  # Redirect to home after updating

    def form_valid(self, form):
        messages.success(self.request, "Event updated successfully!")
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'users/event_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Event deleted successfully!")
        return super().delete(request, *args, **kwargs)


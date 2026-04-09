from django.shortcuts import render, redirect
from django.contrib.auth import login
from reviews.models import Review
from .forms import SignUpForm
from .forms import ContactForm

def home(request):
    latest_reviews = Review.objects.order_by('-created_at')[:3]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"""
New contact form message

Name: {name}
Email: {email}

Message:
{message}
"""

            send_mail(
                subject=f"New message from {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['aivroll@protonmail.com'],
                fail_silently=False,
            )

            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'core/home.html', {
        'latest_reviews': latest_reviews,
        'form': form
    })


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
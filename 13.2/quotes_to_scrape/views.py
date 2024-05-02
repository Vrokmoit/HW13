from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UkrainianUserCreationForm 
from .forms import AuthorForm
from .forms import QuoteForm
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def author_list(request):
    with open('authors.json', 'r') as json_file:
        authors_data = json.load(json_file)
    return render(request, 'author_list.html', {'authors': authors_data})

def home(request):
    with open('quotes.json', 'r') as json_file:
        quotes_data = json.load(json_file)

    return render(request, 'index.html', {'quotes': quotes_data})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm(user=request.user)
    return render(request, 'add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm(user=request.user)
    return render(request, 'add_quote.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UkrainianUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UkrainianUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    html_email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'registration/password_reset_subject.txt'


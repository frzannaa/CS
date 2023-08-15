from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def signupaccount(request):
    form = UserCreationForm()  # Instantiate the UserCreationForm
    return render(request, 'signupaccount.html', {'form': form})

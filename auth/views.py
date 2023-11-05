from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
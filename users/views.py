from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForms

def register(request):
    if request.method == 'POST':
      form = UserRegisterForms(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created! You are now ble to login')
        return redirect('login')
    else:
     form = UserRegisterForms()
    return render(request, 'users/register.html', {'form':form})




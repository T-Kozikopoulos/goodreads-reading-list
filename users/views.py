from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


# Unlike for the Books model, I wrote this without only using Django's built-in forms
# and added some customization, so that now you can see both way to go about it.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account created: {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

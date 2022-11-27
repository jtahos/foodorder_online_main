from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
    
        form = UserForm(request.POST)
        if form.is_valid():
            # create the user using the form
        
            # user = form.save(commit=False)
            # password = form.cleaned_data['password']
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()
            
            # create the user using the createUser method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'your account has been created!')
            
            return redirect('registerUser')
            
        else:
            print('invalid form')
            print('Form.errors')
    else:    
         form = UserForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/registerUser.html', context)
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from .import counsellor,scholarship


def index(request):
    return render(request, 'index.html')

def top(request):
    return render(request, 'top.html')

def after10(request):
    return render(request, 'after10.html')

def counselling(request):
    counsellors = counsellor.counsellors()
    # print(counsellors[0][0])
    return render(request, 'counselling.html', {'counsellors': counsellors})

def trusts(request):
    trusts = scholarship.trusts()
    # print(counsellors[0][0])
    return render(request, 'trusts.html', {'trusts': trusts})

def register(request):
    return render(request, 'register.html')



def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/account')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
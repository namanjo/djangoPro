from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import Topic, Webpage, AccessRecord, UserInfo, UserProfileRegister
from app_one.forms import FormName, SignupForm,UserForm, UserProfileRegisterForm

#Login stuff
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    people_list = UserProfileRegister.objects.all()
    data_dict = {'webpage_list':webpages_list, 'people_list':people_list}
    return render(request, 'app_one/index.html', context=data_dict)

@login_required
def simple_form_users(request):
    user_list = UserInfo.objects.order_by('first_name')
    form_users_list = {'user_list': user_list}
    return render(request, 'app_one/simple_form_users.html', context=form_users_list )

def simple_form_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print('\n****Validation Successfull****')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Message: ' + form.cleaned_data['text'])

    return render(request, 'app_one/form_page.html', {'form':form})

@login_required
def sign_up(request):
    signup = SignupForm()

    if request.method == 'POST':
        signup = SignupForm(request.POST)

        if signup.is_valid():
            signup.save()
            return index(request)
        else:
            print('\nInvalid Input\n')
    return render(request, 'app_one/sign_up.html', {'form_signup': signup})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileRegisterForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileRegisterForm()
    return render(request, 'app_one/registration.html', {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'registered':registered})

#For Login
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active.')
        else:
            print('\nSomeone tried to login and failed.\n')
            return HttpResponse('Invalid Login details supplied.')
    else:
        return render(request, 'app_one/login.html')

#For logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

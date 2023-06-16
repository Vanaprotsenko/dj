from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import User

# Create your views here.


def register(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if User.objects.filter(username = username, password=password).exists():
            context['in_bd'] = 'Такий користувач вже існує,ви можете залишити свій коментарь'
            
        else:

            if name and surname and username and password and confirm_password:
                if len(password) >= 8:
                    if password == confirm_password:
                        try:
                            User.objects.create(name=name,username=username,surname=surname,password=password,confirm_password=confirm_password)
                        except IntegrityError:
                            context['error'] = 'Такий користувач вже існує'

                    else:
                        context['error'] = 'Паролі не співпадають'
                else:

                    context['error'] ='Пароль повинен бути 8 або більше символів'
            else:
                context['error'] = 'Заповнити усі поля'
    return render(request,'user/register.html',context)



def auth(request):
    context ={}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username, password=password).exists():
            context['accept'] = 'Можете залишити свій коментарь'
        else:
            return redirect('main')

    return render (request, 'user/auth.html', context)






# def auth(request):
    # if request.user.is_authenticated:
    #     return redirect('main')

    # context ={}
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(username = username, password = password)
    #     if user:
    #         login(request,user)
    #     else:
    #         context['error']="Логін чи пароль неправильні"

    # return render(request, 'user/auth.html',context)
    

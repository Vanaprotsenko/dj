from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from user.models import User
from .models import Revie


# Create your views here.


def revie(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        review = request.POST.get('review')
        if User.objects.filter(username=username).exists():
            try:
                Revie.objects.create(username=username,review=review)
                context['accept'] = ' Такий користувач зареїстрован ви можете залишити відгук'
            except IndentationError:
                context['accept'] = 'Такого юзернайма не існує'
        else:
            return redirect('main')
        
    return render(request, 'reviews/revie.html', context)
            



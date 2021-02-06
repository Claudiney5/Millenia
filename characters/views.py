from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    characters = Character.objects.all()
    form = CharacterForm()

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/characters')

    context = {'characters': characters, 'form': form}

    return render(request, 'characters/list.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home_jumia(request):
    return HttpResponse("Welcome home of jumia")


@login_required(login_url='note/note')
def author(request):
    return render(request, 'jumia/welcome.html', {})


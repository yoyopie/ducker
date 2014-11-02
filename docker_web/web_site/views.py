from django.shortcuts import render_to_response
from django.http import HttpResponse
import models

# Create your views here.


def index(request):
    return HttpResponse('Hello world!')

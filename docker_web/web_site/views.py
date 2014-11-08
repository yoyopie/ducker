from django.shortcuts import render_to_response
from django.http import HttpResponse
import models
import docker

# Create your views here.


def index(request):
    c = docker.Client(base_url='unix://var/run/docker.sock', version='1.9', timeout=10)
    images = c.images()
    context = {
        'images': images,
    }
    return render_to_response('index.html', context)


def containers(request):
    c = docker.Client(base_url='unix://var/run/docker.sock', version='1.9', timeout=10)
    containers = c.containers(all=True)
    context = {
        'containers': containers,
    }
    return render_to_response('containers.html', context)

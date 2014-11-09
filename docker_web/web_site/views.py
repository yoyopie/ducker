from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import models
import docker

# Create your views here.


@login_required
def index(request):
    c = docker.Client(base_url='unix://var/run/docker.sock', version='1.9', timeout=10)
    images = c.images()
    user = request.user
    context = {
        'images': images,
        'user': user,
    }
    return render_to_response('index.html', context)


@login_required
def containers(request):
    c = docker.Client(base_url='unix://var/run/docker.sock')
    if request.method == "POST":
        containerid = request.POST.get('containerid', '')
        action = request.POST.get('submit', '')
        if action == 'start':
            c.start(containerid)
        elif action == 'stop':
            c.stop(containerid)
        else:
            c.restart(containerid)
    containers = c.containers(all=True)
    user = request.user
    context = {
        'containers': containers,
        'user': user,
    }
    return render_to_response('containers.html', context)

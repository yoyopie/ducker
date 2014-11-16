from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import models
import docker
import forms

# Create your views here.


@login_required
def index(request):
    c = docker.Client(base_url='unix://var/run/docker.sock', version='1.9', timeout=10)
    images = c.images()
    user = request.user
    host = models.Hostinfo.objects.all()
    context = {
        'images': images,
        'user': user,
        'host': host,
    }
    return render_to_response('index.html', context)


def ajaximages(request):
    hostip = request.GET.get('hostip', '')
    c = docker.Client(base_url='tcp://' + hostip + ':2375', timeout=10)
    images = c.images()
    context = {
        'images': images,
    }
    return render_to_response('ajaximages.html', context)


def ajaxcontainers(request):
    hostip = request.GET.get('hostip', '')
    c = docker.Client(base_url='tcp://' + hostip + ':2375', timeout=10)
    containers = c.containers(all=True)
    context = {
        'containers': containers,
    }
    return render_to_response('ajaxcontainers.html', context)


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
    host = models.Hostinfo.objects.all()
    context = {
        'containers': containers,
        'user': user,
        'host': host,
    }
    return render_to_response('containers.html', context)


@login_required
def host(request):
    hostform = forms.HostForm()
    if request.method == "POST":
        hostform = forms.HostForm(request.POST)
        if hostform.is_valid():
            hostform.save()
    host = models.Hostinfo.objects.all()
    context = {
        'hostform': hostform,
        'host': host,
    }
    return render_to_response('host.html', context)

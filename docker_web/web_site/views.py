from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import models
import docker
import forms

# Create your views here.


@login_required
def index(request):
    hostip = ''
    errorinfo = ''
    try:
        hostip = models.Hostinfo.objects.all()[0].ip
    except:
        errorinfo = 'No host in models,please add host!'
    c = docker.Client(base_url='tcp://' + hostip + ':2375', timeout=10)
    images = c.images()
    user = request.user
    host = models.Hostinfo.objects.all()
    context = {
        'images': images,
        'user': user,
        'host': host,
        'errorinfo': errorinfo,
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


@login_required
def containers(request):
    hostip = ''
    errorinfo = ''
    if request.method == "GET":
        hostip = request.GET.get('hostip', '')
    else:
        try:
            hostip = models.Hostinfo.objects.all()[0].ip
        except:
            errorinfo = 'No host in models,please add host!'
    c = docker.Client(base_url='tcp://' + hostip + ':2375', timeout=10)
    if request.method == "POST":
        containerid = request.POST.get('containerid', '')
        action = request.POST.get('submit', '')
        hostip = request.POST.get('controlhost', '')
        c = docker.Client(base_url='tcp://' + hostip + ':2375', timeout=10)
        if action == 'start':
            c.start(containerid)
        elif action == 'stop':
            c.stop(containerid)
        elif action == 'delete':
            c.stop(containerid)
            c.remove_container(containerid)
        #elif action == 'console':
        #    return HttpResponseRedirect('https://' + hostip + ':5400')
        elif action == 'restart':
            c.restart(containerid)
        if request.POST.get('submit1'):
            name = request.POST.get('name', '')
            #port = request.POST.get('port', '')
            imageid = request.POST.get('imageid', '')
            c.create_container(image=imageid, name=name)
    try:
        images = c.images()
        containers = c.containers(all=True)
    except:
        return HttpResponseRedirect('/host/')
    user = request.user
    host = models.Hostinfo.objects.all()
    containerform = forms.ContainerForm()
    context = {
        'images': images,
        'containers': containers,
        'user': user,
        'host': host,
        'hostip': hostip,
        'errorinfo': errorinfo,
        'containerform': containerform,
    }
    return render_to_response('containers.html', context)


@login_required
def host(request):
    hostform = forms.HostForm()
    if request.method == "POST":
        action = request.POST.get('submit', '')
        delhostip = request.POST.get('delhostip', '')
        hostform = forms.HostForm(request.POST)
        if hostform.is_valid() and action == "Add":
            hostform.save()
        if action == "Delete":
            hostobjects = models.Hostinfo.objects.filter(ip=delhostip)
            hostobjects.delete()
    host = models.Hostinfo.objects.all()
    context = {
        'hostform': hostform,
        'host': host,
    }
    return render_to_response('host.html', context)

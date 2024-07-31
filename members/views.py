from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

# Create your views here.
def members(request):
    template = loader.get_template(template_name='myfirst.html')
    return HttpResponse(template.render())

def all_members(request):
    allmembers = models.Member.objects.all()
    return render(request=request, template_name='all_members.html', context={'members': allmembers.values()})

def details(request, slug):
    mymember = models.Member.objects.get(slug=slug)
    tmp = loader.get_template('details.html')
    ctx = {'mymember': mymember}
    return HttpResponse(tmp.render(context=ctx, request=request))

def main(request):
    return render(request=request, template_name='main.html', context={})

def testing(request):
    tmp = loader.get_template('template.html')
    words = ['foo', 'bar', 'baz', 'zap', 'wobble', 'fizzle', 'trax']
    ctx = {'words': words, 'name': 'Diyorbek'}
    return HttpResponse(tmp.render(context=ctx, request=request))

def members_table(request):
    tbe = models.Member.objects.all()
    return render(request=request, template_name='members_table.html', context={'table_members': tbe.values()})
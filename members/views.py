from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages as msg
from . import models, forms

# Create your views here.
def members(request):
    template = loader.get_template(template_name='myfirst.html')
    return HttpResponse(template.render())

def all_members(request):
    all_members = models.Member.objects.all()
    return render(request=request, template_name='all_members.html', context={'members': all_members})

def details(request, slug):
    my_member = models.Member.objects.get(slug=slug)
    tmp = loader.get_template('details.html')
    ctx = {'member': my_member}
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

def add_member(request):
    if request.method == 'POST':
        form = forms.MemberForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            msg.success(request, 'Member added successfully.')
            return redirect('all_members')
        else:
            msg.warning(request, 'Failed to add member.')
    else:
        form = forms.MemberForm()
    return render(request, 'add_member.html', {'form': form})

def update_member(request, slug):
    member = get_object_or_404(models.Member, slug=slug)
    if request.method == 'POST':
        form = forms.MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            msg.success(request, 'Member updated successfully.')
            return redirect('all_members')
        else:
            msg.warning(request, 'Failed to update member.')
    else:
        form = forms.MemberForm(instance=member)
    return render(request, 'update_member.html', {'form': form, 'member': member})

def delete_member(request, slug):
    member = get_object_or_404(models.Member, slug=slug)
    member.delete()
    msg.success(request, 'Member deleted successfully.')
    return redirect('all_members')

def search_member(request):
    query = request.GET.get('query', '')  # Get the search query from the request.
    members = []  # Initialize an empty list to hold search results.

    if query:
        members = models.Member.objects.filter(firstname__icontains=query)  # Perform a case-insensitive search.

    return render(request, 'search_member.html', {'members': members, 'query': query})


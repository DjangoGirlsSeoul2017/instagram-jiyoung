from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

def detail(request, pk, hidden=False):
    if hidden is True:
        # TODO:
        pass

    photo = get_object_or_404(Photo, pk=pk)
    # photo = Photo.objects.get(pk=pk)
    url = photo.image.url
    content = {
        'url' : url,
        'photo' : photo,
        }
    return render(request, 'photos/index.html', content)
    # return redirect(detail)

def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    context = {
        'form' : form,
    }
    return render(request, 'edit.html', context)

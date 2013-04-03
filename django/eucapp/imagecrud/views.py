from django.http import HttpResponse
from django.utils import timezone
from imagecrud.models import Image
from django import forms

import os

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Eucalyptus Image CRUD!")

img_dir = '/tmp/image_crud/'

def store_uploaded_file(f, name):
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    path = '%s%s' % (img_dir,name)
    with open(path , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path

def create(request, image_name):
    if not request.method == 'POST':
        return HttpResponse(status=405)
    try:
        image=Image.objects.get(name=image_name)
        return HttpResponse(status=405)
    except Image.DoesNotExist:
        form = UploadFileForm(request.POST, request.FILES)
        path = None
        if form.is_valid():
            try:
                path = store_uploaded_file(request.FILES['file'], image_name)
            except:
                return HttpResponse(status=500)
            img = Image(name=image_name,pub_date=timezone.now(),path=path)
            img.save()
            return HttpResponse('image %s created' % image_name, status=200)
        else:
            return HttpResponse(status=405)

def read(request, image_name):
    return HttpResponse("you are reading %s" % image_name)

def update(request, image_name):
    return HttpResponse("you are updating %s" % image_name)

def delete(request, image_name):
    try:
        image=Image.objects.get(name=image_name)
        image.delete()
        return HttpResponse('image %s deleted' % image_name, status=200)
    except Image.DoesNotExist:
        return HttpResponse(status=404)
    except Exception, err:
        return HttpResponse(status=500)

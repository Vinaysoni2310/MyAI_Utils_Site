from django.shortcuts import render
from .models import BGRemover
from .forms import UploadFileForm
from django.http import HttpResponse
from rembg import remove
from PIL import Image


def index(request):
    # print(BGRemover.objects.all().values())
    # BGRemover.objects.all().delete()
    return render(request, 'index.html')

def BgRemove(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            image = f.Image
            input_img = Image.open(image)
            output = remove(input_img)
            output_path = 'media/remove_bg/img1.png'
            output.save(output_path)
            return render(request, 'test.html', {'form': form, 'image':image,'output':output_path})
    else:
        form = UploadFileForm()
        return render(request, 'test.html',{'form': form})

def uploadImage(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = UploadFileForm()
        images = BGRemover.objects.all()
        return render(request, 'services.html', {'form': form, 'images':images})

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')


from django.shortcuts import render
from .models import BGRemover
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# obj = get_object_or_404(BGRemover, id=1)



def index(request):
    #print(BGRemover.objects.all().values())
    #BGRemover.objects.all().delete()
    return render(request, 'index.html')

def BgRemove(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            image = f.Image
            return render(request, 'test.html', {'form': form, 'image':image})
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


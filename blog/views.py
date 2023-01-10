from django.shortcuts import render
from .forms import adminManage
from .models import musicUploader
from django.http import HttpResponse
def home(request):
  data = musicUploader.objects.all()
  return render(request, 'blog.html', {"data":data})
  
def admin_login(request):
  if request.method == "POST":
    x = adminManage(request.POST, request.FILES)
    if x.is_valid():
      x.save()
      return HttpResponse("saved")
  form = adminManage
  return render(request, 'admin.html', {'form':form})
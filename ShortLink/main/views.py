from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
# Create your views here.

def home(request):
    if request.method  =="POST":
        url = request.POST.get("url")
        obj = ShortURL.objects.create(original_url=url)
        return render(request, "main/home.html", {"short_url": request.build_absolute_uri("/") + obj.short_code})
    return render(request, "main/home.html")

def redirect_url(request, shortcode):
    obj = get_object_or_404(ShortURL, short_code=shortcode)
    return redirect(obj.original_url)
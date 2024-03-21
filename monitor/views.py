from django.shortcuts import render, redirect
from .forms import URLForm
from .models import URLStatus
from django.utils.timezone import now
import requests

def add_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.head(url, timeout=5)
                status = response.status_code == 200
            except requests.RequestException:
                status = False
            
            URLStatus.objects.create(url=url, status=status, last_checked=now())
            return redirect('url_list')  # Redirect to the URL list view
    else:
        form = URLForm()
    return render(request, 'monitor/add_url.html', {'form': form})

def url_list(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.head(url, timeout=5)
                status = response.status_code == 200
            except requests.RequestException:
                status = False
            URLStatus.objects.create(url=url, status=status, last_checked=now())
            return redirect('url_list')  # Redirect back to the URL list page to show the updated list
    else:
        form = URLForm()

    urls = URLStatus.objects.all()
    return render(request, 'monitor/url_list.html', {'form': form, 'urls': urls})

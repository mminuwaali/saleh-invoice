from django.shortcuts import render
from .models import Member

# Create your views here.
def home_view(request):
    return render(request, 'main/index.html', {'members':Member.objects.all()})

def detail_view(request, id):
    return render(request, 'main/detail.html', {'member':Member.objects.get(id=id)})


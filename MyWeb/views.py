from django.shortcuts import render

# Create your views here.
from .models import PictureTable
from django.shortcuts import redirect


def index(request):
    pic_list = PictureTable.objects.all().order_by('-create_time')
    context = {'post_list': pic_list,
               }

    return render(request, 'MyWeb/index.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Language

# Create your views here.
def index(request):
    polls = Language.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'polls': polls,
    }
    return HttpResponse(template.render(context, request))
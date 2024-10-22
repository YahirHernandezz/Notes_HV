# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.base import TemplateView

# def home(request):
#     return HttpResponse("Hola mundo")

class HomePageView(TemplateView):
    template_name = "notes/home.html"


 
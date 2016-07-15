from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {"user":'devin', 'level':3})
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomePage(View):
    greeting = "Hi from Parent"

    def get(self, request):
        return HttpResponse(self.greeting)
    

class ChildPage(HomePage):
    def get(self, request):
        self.greeting = "Hi from Child"

        return HttpResponse(self.greeting)

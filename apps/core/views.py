from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Count
import datetime

from core.forms import LoginForm
from core.models import Publisher, Book

class HomePage(TemplateView):
    template_name = "core/main_page.html"
    

class ChildPage(HomePage):
    def get(self, request):
        self.greeting = "Hi from Child"

        return HttpResponse(self.greeting)


class SettingsView(TemplateView):
    template_name = "core/settings.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def LoginView(request):
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponse("Post login")
    return render(request, "core/login.html", {"form": form})


class PublisherListView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

from typing import Any
from django.shortcuts import render, redirect
from .models import Aweitr
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm
from .forms import *
# Create your views here.

def index(request):
    new_post = Aweitr.objects.order_by('-data')
    return render(request, "main/hom.html", {"new_post": new_post})


class nowels(DetailView):
    model = Aweitr
    template_name = "main/dino.html"
    context_object_name = "post"

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        # c_def = self.get_user_context(titlt = "Авторизацыя")
        return dict(list(context.items()))

    # def get_success_url(self):
    #     return reverse_lazy('home')


def create(request):
    error = ""
    if request.method == "POST":
        form = Ahop(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была не верной"

    form = Ahop()

    date = {
        "form": form,
        "error": error,
    }
    return render(request, "main/forma.html", date)


class delete(DeleteView):
    model = Aweitr
    template_name = "main/delete.html"
    success_url = "/"
    # fields = ["title", "anons", "text", "data"]

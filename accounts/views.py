from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from accounts.forms import UserLoginForm


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "accounts/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("website:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class(request)})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return redirect("website:home")
        return render(request, self.template_name, {"form": form})

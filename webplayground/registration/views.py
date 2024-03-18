from .forms import UserCreationFormWithEmail
from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms

# Create your views here.


class SinUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = "registration/signup.html"

    def get_success_url(self) -> str:
        return reverse_lazy("login") + "?register"

    def get_form(self, form_class: type[BaseModelForm] | None = ...) -> BaseModelForm:
        form = super(SinUpView, self).get_form()
        # Modificar en tiempo real
        form.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control mb-2", "placeholder": "Nombre de usuario"}
        )
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2", "placeholder": "Email"}
        )
        form.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Contraseña"}
        )
        form.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Repite contraseña"}
        )
        return form


@method_decorator(login_required, name="dispatch")
class ProfileUpdate(TemplateView):
    template_name = "registration/profile_form.html"

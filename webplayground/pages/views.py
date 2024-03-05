from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect


class StaffRequiredMixin(object):
    """Este mixin requiere que el usuario sea meibro del staff"""

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if not request.user.is_staff:
            return redirect(reverse_lazy("admin:login"))
        return super().dispatch(request, *args, **kwargs)


# Create your views here.


class PageListView(ListView):
    model = Page


class PageDetailView(StaffRequiredMixin, DetailView):
    model = Page


class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("pages:pages")


class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return reverse_lazy("pages:update", args=[self.object.id]) + "?ok"


class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")

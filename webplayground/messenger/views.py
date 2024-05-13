from typing import Any
from django.db.models.base import Model as Model
from django.views.generic.detail import DetailView
from .models import Thread
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404

# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"


class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail).get_object()
        if self.request.user not in obj.users.all():
            raise Http404
        return obj

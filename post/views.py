# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = 'post/top.html'

class FrontView(LoginRequiredMixin,TemplateView):
    template_name = 'post/front.html'

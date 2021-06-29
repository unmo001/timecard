# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import resolve_url, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, CreateView

from post.forms import TimeForm
from registration.models import CommutingTime


class TopView(TemplateView):
    template_name = 'post/top.html'

# やりたいこと、ボタンでユーザーに出社時間を記録させること
# まずはユーザーにリレーショナルで出社時間モデルを紐づける
class FrontView(LoginRequiredMixin,CreateView):
    model = CommutingTime
    form_class = TimeForm

    def form_valid(self, form):
        post = form.save(commit=True)
        post.user = self.request.user
        post.arrive_at_work = timezone.now()
        post.save()
        return redirect('post:front')



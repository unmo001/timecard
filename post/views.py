# Create your views here.

from datetime import date
from itertools import chain

from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView, CreateView

from registration.models import CommutingTime


class TopView(TemplateView):
    template_name = 'post/top.html'


# やりたいこと、ボタンでユーザーに出社時間を記録させること
# まずはユーザーにリレーショナルで出社時間モデルを紐づける
class FrontView(CreateView):
    template_name = 'post/front.html'
    model = CommutingTime
    fields = []

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user

        if "arrive_at_work" in self.request.POST:
            aaw = self.request.POST['arrive_at_work']
            post.arrive_at_work = timezone.datetime.today()
            if CommutingTime.objects.filter(user=self.request.user, arrive_at_work__istartswith=date.today()):
                return redirect('post:front')
            else:
                post.CommutingTime = CommutingTime(arrive_at_work=aaw)
                post.save()
            return redirect('post:front')
        else:
            CommutingTime.objects.filter(user=self.request.user, leave=None,
                                         arrive_at_work__isnull=False).update(leave=timezone.datetime.today())
            return redirect('post:front')

    def get_context_data(self, **kwargs):
        context = super(FrontView, self).get_context_data(**kwargs)
        context['commuting_times'] = CommutingTime.objects.filter(user=self.request.user, )


        return context

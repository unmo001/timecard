from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from registration.forms import LoginForm, SignUpForm


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'registration/login.html'


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    user = get_user_model()

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('registration:login')
        return render(request, 'registration/signup.html', {'form': form})

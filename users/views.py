from django.shortcuts import render, redirect
from django. urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, View, CreateView
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm
from users.models import User
   

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            image_user = form.cleaned_data['image_user'],
            link = form.cleaned_data['link']
                  )
                
        return super(UserRegisterView, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:user_panel')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('index')


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user_login')
    login_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()



            logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


############################################ PANEL #############################################################


class PanelPage(LoginRequiredMixin, TemplateView):
    template_name = "users/panel.html"
    login_url = reverse_lazy('users_app:user_login')
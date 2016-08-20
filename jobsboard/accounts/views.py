from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from . import forms


class Signup(TemplateView):
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.CreateUser()
        return context

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated():
            return redirect('index')
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = forms.CreateUser(self.request.POST, instance=User())
        if not form.is_valid():
            context['form'] = form
            return render(request, self.template_name, context)
        form.save()
        return redirect('accounts:login')


class ProfileUpdate(TemplateView):
    template_name = 'accounts/profile_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        form = forms.ProfileUpdate(instance=user, initial=initial)
        context['initial'] = initial
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user = self.request.user
        form = forms.ProfileUpdate(
            self.request.POST,
            instance=user,
            initial=context.get('initial'),
        )
        if form.is_valid():
            form.save()
        context['form'] = form
        return render(request, self.template_name, context)

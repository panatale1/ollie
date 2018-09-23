'''Views for Ollie code screen'''

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, CreateView

from .forms import OllieSignUpForm
from .models import OllieUser


class SignUpView(CreateView):
    form_class = OllieSignUpForm
    model = OllieUser

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        user = self.object
        user.save()
        return response

    def get_success_url(self):
        return reverse('sign-up-success')


class SignUpSuccess(TemplateView):
    template_name = 'ollie/sign_up_success.html'

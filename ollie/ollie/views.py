'''Views for Ollie code screen'''

from django.views.generic import FormView

from .forms import InfoForm


class SignUpView(FormView):
    form_class = InfoForm

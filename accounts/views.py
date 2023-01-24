# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.conf import settings
from django.core.mail import send_mail


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        user = form.cleaned_data.get("username")
        send_mail('Cookify signup', f'Hello {user}, Thank you for signing up', settings.EMAIL_HOST_USER, [email], False)
        return super(SignUpView, self).form_valid(form)


# def send_authentication_email(request):
#
#     if request.method == "POST":
#
#         send_mail("Test", "Hi", settings.EMAIL_HOST_USER, ['popot64981@ukbob.com'], False)

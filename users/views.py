from django.shortcuts import render
from django.views import View

from users.forms import UserRegistrationForm

class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = "registration/registor.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, self.template_name, {'form': form})
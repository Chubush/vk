from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.models import Gamers
from account.forms import CreateUserForm, LoginForm, UpdateUserForm
from base64 import urlsafe_b64encode
from django.utils.encoding import force_bytes, force_str
from account.token import user_tokenizer_generate
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required


#registerview
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid(): 

            user = form.save()
            user.is_active = False
            user.save()

            # Email verification setup (template)
            current_site = get_current_site(request)

            subject = 'Hesap doğrulama e-postası'

            message = render_to_string('account/registration/email-verification.html', {
            
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            
            })
            user.email_user(subject=subject, message=message)


            return redirect('email-verification-sent')
        
    context = {'form':form}
    
    return render(request, 'account/registration/register.html', context=context)

def email_verification(request, uidb64, token):

    # uniqueid

    unique_id = force_str(urlsafe_base64_decode(uidb64))

    user = User.objects.get(pk=unique_id)
    
    # Success

    if user and user_tokenizer_generate.check_token(user, token):

        user.is_active = True

        user.save()

        return redirect('email-verification-success')


    # Failed 

    else:

        return redirect('email-verification-failed')
        
        
class EmailVerificationSentView(TemplateView):
    template_name = "account/registration/email-verification-sent.html"
    
class EmailVerificationSuccessView(TemplateView):
    template_name = "account/registration/email-verification-success.html"
    
class EmailVerificationFailedView(TemplateView):
    template_name = "account/registration/email-verification-failed.html"


class LoginView(FormView):
    template_name = "account/my-login.html"
    form_class = LoginForm
    
    def form_valid(self, form):
        
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return redirect("dashboard")
        
        return super().form_invalid(form)
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "account/dashboard.html"
    


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        request.session.flush()
        return redirect("user-logout")   

class UserLogoutView(TemplateView):
    template_name = "account/user-logout.html" 
    
class ProfileManagementView(UpdateView):
    model = Gamers
    form_class = UpdateUserForm
    template_name = 'account/profile-management.html'
    success_url = reverse_lazy('succes')

    def get_object(self, queryset=None):
        user = self.request.user
        if hasattr(user, 'gamer'):
            return user.gamer
        else:
            gamer = Gamers(username=user)
            gamer.save()
            return gamer
    

        
       
            
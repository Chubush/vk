from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from account.models import Gamers, Games


#register form
class CreateUserForm(UserCreationForm):
        
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
            
            
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
            
        self.fields["email"].required = True
            
    #email validation
        
    def clean_mail(self):
            
        email = self.cleaned_data.get("email")
            
        if User.objects.filter(email=email).exists():
                
            raise forms.ValidationError("This email is invalid")
            
        if len(email) >= 350:
                
            raise forms.ValidationError("Your email is too long")
            
        return email
        
        
# login Form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
        
        
# update form

class UpdateUserForm(forms.ModelForm):
    games_played = forms.ModelMultipleChoiceField(
        queryset=Games.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Gamers
        fields = ['age', 'profile_image', 'best_game', 'games_played']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
            'best_game': forms.Select(attrs={'class': 'form-control'}),
        }
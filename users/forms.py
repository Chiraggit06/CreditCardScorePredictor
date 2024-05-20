from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile,predict_model
gender_choices=[
    (1,'Male'),(2,'Female')
]

edu_choices=[
    (1,'Graduate'),(2,'University'),
    (3,'High School'),(4,'others'),
    (5,'Unknown')
]

marital_choices=[
    (1,'Married'),(2,'Single'),(3,'other')
]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class predict_form(forms.Form):
     gender=forms.CharField(max_length=10,widget=forms.RadioSelect(choices=gender_choices,attrs={'style':'margin-left: 10px;','class':'form-check-inline'}))
     education=forms.CharField(max_length=10,widget=forms.RadioSelect(choices=edu_choices,attrs={'style':'margin-left: 10px;','class':'form-check-inline'}))
     marital_status=forms.CharField(max_length=10,widget=forms.RadioSelect(choices=marital_choices,attrs={'style':'margin-left: 10px;','class':'form-check-inline'}))
     age=forms.CharField(max_length=10,)
     limit=forms.CharField(max_length=10)
     repay_april=forms.IntegerField(min_value=-2,max_value=9,)
     repay_may=forms.IntegerField(min_value=-2,max_value=9,)
     repay_june=forms.IntegerField(min_value=-2,max_value=9,)
     repay_july=forms.IntegerField(min_value=-2,max_value=9,)
     repay_aug=forms.IntegerField(min_value=-2,max_value=9,)
     repay_sep=forms.IntegerField(min_value=-2,max_value=9,)
     bill_april=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     bill_may=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     bill_june=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     bill_july=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     bill_aug=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     bill_sep=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     prev_april=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     prev_may=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     prev_june=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     prev_july=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     prev_aug=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     prev_sep=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'style':'width: 100px;'}))
     


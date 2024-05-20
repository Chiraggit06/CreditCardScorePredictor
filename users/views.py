from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import predict_model
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm,predict_form
from django.shortcuts import render
import pickle
import numpy as np
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
def blog_list(request):
    return render(request, 'users/blog_list.html')
def service(request):
    return render(request, 'users/service.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send an email (for simplicity, we print to the console)
          
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'users/contact.html', {'form': form})


def about(request):
    return render(request, 'users/about.html')

def main(request):
    return render(request, 'users/main.html')

def home(request):
    form=predict_form()
    return render(request, 'users/home.html',{'form':form})

def predict(request):
    model = pickle.load(open('users/model/model.pkl', 'rb'))
    pred_model=predict_model()
    if request.method=="POST":
        form=predict_form(request.POST)
        if form.is_valid():
            features = [int(x) for x in form.cleaned_data.values()]
            print(features)
            
            feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
            features_arr = [np.array(feature_list)]
            print(features_arr)

            prediction = model.predict(features_arr)

            print(features_arr)
            #newdb.insert_one(d)
            print("features is :",features)
            default_payment=prediction.tolist()
            result = ""
            if prediction == 1:
                result = "The credit card holder will be Defaulter in the next month"
            else:
                result = "The Credit card holder will not be Defaulter in the next month"
            
            pred_model.gender=features[0]
                    
            pred_model.education=features[1]
            pred_model.marital_status=features[2]
            pred_model.age=features[3]
            pred_model.limit=features[4]
            pred_model.repay_april=features[5]
            pred_model.repay_may=features[6]
            pred_model.repay_june=features[7]
            pred_model.repay_july=features[8]
            pred_model.repay_aug=features[9]
            pred_model.repay_sep=features[10]
            pred_model.bill_april=features[11]
            pred_model.bill_may=features[12]
            pred_model.bill_june=features[13]
            pred_model.bill_july=features[14]
            pred_model.bill_aug=features[15]
            pred_model.bill_sep=features[16]
            pred_model.prev_april=features[17]
            pred_model.prev_may=features[18]
            pred_model.prev_june=features[19]
            pred_model.prev_july=features[20]
            pred_model.prev_aug=features[21]
            pred_model.prev_sep=features[22]
            pred_model.default_pay=default_payment

            pred_model.save()
          
            messages.success(request, result)
            return redirect(to='users-home')
        
    return HttpResponse("Nothing happend")

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')
             

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
        
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

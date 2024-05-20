from django.urls import path
from .views import home,main, profile, RegisterView,predict,contact,about,blog_list,service

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('predict/',predict,name="predict"),
    path('main/',main,name="main"),
     path('contact/',contact, name='contact'),
     path('about/', about, name='about'),
        path('blog/',blog_list, name='blog_list'),
        path('service/',service, name='service'),
]

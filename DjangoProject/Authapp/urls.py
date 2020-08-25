from django.urls import path, include
from Authapp import views

app_name = 'Authapp'
urlpatterns = [
    path('login/',views.login_page, name='login_page'),
    path('registeration',views.registeration,name='registeration'),
]

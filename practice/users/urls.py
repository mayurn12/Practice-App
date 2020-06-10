from django.urls import path
from users import views as users_view

urlpatterns=[
    path('/',users_view.Register, name ='register')
]
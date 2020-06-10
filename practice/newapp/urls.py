from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('addname',views.CreateName.as_view(),name='addname'),
    path('namelist',views.namelist,name='namelist'),
    path('<int:pk>/',views.DetailsNameView.as_view(), name = 'details'),
    path('upd/<int:id>',views.updatename, name='update'),
    path('dlt/<int:id>',views.deletename,name = 'delete'),
]
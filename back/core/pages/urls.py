from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('reservation/', views.ReservationView.as_view(), name='reservation_page')

]

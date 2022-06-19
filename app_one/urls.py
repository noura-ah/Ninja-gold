from django.urls import path, include
from . import views

urlpatterns = [
    path('start',views.start,name='start'),
    path('',views.index,name='index'),
    path('process_<str:process>',views.process_money,name='process_money'),
    path('destroy',views.destroy,name='destroy'),
    # using form method
    # path('process_money',views.process_money)
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.landin),
    path('refresh/',views.script_run),
    path('crypt-currencies/',views.CurrencyList.as_view()),
]

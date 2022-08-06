from django.urls import path
from .views import main, moving, delivery, terms_and_conditions

urlpatterns = [
    path('', main, name='main'),
    path('moving/', moving, name='moving'),
    path('delivery/', delivery, name='delivery'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),
]
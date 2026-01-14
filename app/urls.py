
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),       # ← homepage FIXED
    path('home/', index, name='home'),   # optional
]

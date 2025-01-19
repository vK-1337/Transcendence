print("loading urls.py")
from django.urls import path
from . import views
print("printed, defining urlpatterns")

urlpatterns = [
    path('', views.index, name='index'),
]
print("done: ", urlpatterns)

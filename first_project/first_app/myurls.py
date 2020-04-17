from django.urls import path
from first_app import views

urlpatterns = [
path('url1',views.index,name="index"),
path('url2',views.help,name="help"),
path('img',views.baseimg,name="image")
]

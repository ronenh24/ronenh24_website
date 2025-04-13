from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("home.urls"), name="home"),
    path('bible-search/', include("search.urls"), name="bible-search"),
    path('admin/', admin.site.urls),
]

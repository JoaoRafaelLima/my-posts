
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("back_end.apps.usuarios.urls")),
    path('', include("back_end.apps.posts.urls")),
    path('admin/', admin.site.urls),
]

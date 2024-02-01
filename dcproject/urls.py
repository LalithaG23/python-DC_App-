from django.contrib import admin
from django.urls import path
from dcapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.showform),
    path("savedata/",views.savedata),
    path("remove/<int:id>",views.removedata)
]
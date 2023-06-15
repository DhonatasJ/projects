from django.contrib import admin
from django.urls import path
from agendamento.views import agendamento

urlpatterns = [
    path('', agendamento, name='home'),
    path('admin/', admin.site.urls),
]

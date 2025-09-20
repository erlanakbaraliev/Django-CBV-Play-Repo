from django.urls import path

from apps.dmx_admin import views

app_name = 'dmx_admin'

urlpatterns = [
    path('', views.DmxAdminSummaryView.as_view(), name='dmx_admin_home'),
]
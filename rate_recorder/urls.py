from django.urls import path

from rate_recorder import views

app_name = 'rate_recorder'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('search_rates/', views.search_rates_by_date, name='search'),
]

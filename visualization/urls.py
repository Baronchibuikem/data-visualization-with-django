from django.urls import path

from visualization import views


app_name = 'visualization'

urlpatterns = [
    # home
    path('', views.IndexView.as_view(), name="home"),
    path('visual/', views.DataVisualizationView.as_view(), name='visuals'),
]

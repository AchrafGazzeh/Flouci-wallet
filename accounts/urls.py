from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('register/',views.registerpage, name='register'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('',views.landing),
    path('records/',views.record, name='records'),
    path('reports/',views.reports, name='reports'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('reports/delete/<str:delete_id>/', views.delete, name='delete'),
    path('api/linechart/data/',views.LineChartData.as_view()),
    path('api/barchart/data/',views.BarChartData.as_view()),
    path('api_schema',get_schema_view(title='API Schema', description='Guide for the REST API'),name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]
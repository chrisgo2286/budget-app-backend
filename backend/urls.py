"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from budget import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryView, 'category')
router.register(r'ledger_items', views.LedgerItemView, 'ledger_item')
router.register(r'budget_items', views.BudgetItemView, 'budget_item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/ledger/', views.ledger_view),
    path('api/budget/', views.budget_view),
    path('api/reports/monthly_stats/', views.monthly_stats_view),
    path('api/reports/yearly_stats/', views.yearly_stats_view),
    path('api/reports/current_expense_chart/', views.current_expense_chart_view),
    path('api/reports/monthly_expense_chart/', views.monthly_expense_chart_view),
    path('api/reports/monthly_savings_chart/', views.monthly_savings_chart_view),
    path('api/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls'))
]

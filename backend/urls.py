"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('backend.accounts.urls')),

    
    # Attendance
    path('api/attendance/', include('backend.attendance.urls')),


    # Commission
    path('api/commissions/', include('backend.commissions.urls')),


      # Company
    path('api/companies/', include('backend.companies.urls')),


    # Employees
    path('api/employees/', include('backend.employees.urls')),


    # MLM Hierarchy
    path('api/hierarchy/', include('backend.hierarchy.urls')),


    # Notifications
    path('api/notifications/', include('backend.notifications.urls')),


    # Performance
    path('api/performance/', include('backend.performance.urls')),


    # Promotions
    path('api/promotions/', include('backend.promotions.urls')),


    # Reports
    path('api/reports/', include('backend.reports.urls')),


    # Salary
    path('api/salary/', include('backend.salary.urls')),


    # Wallet
    path('api/wallet/', include('backend.wallet.urls')),


    


    
]

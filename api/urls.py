"""doctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from doctor.factories import doctor_view

from .views import ViewWrapper

urlpatterns = [
    path('admin/', admin.site.urls),

    path('doctor/<int:id>',
        ViewWrapper.as_view(view_func=doctor_view),
        name='doctor'),
    
    re_path(r'^doctor/(?P<district>[0-9]+)',
        ViewWrapper.as_view(view_func=doctor_view),
        name='doctor'),
    
    re_path(r'^doctor/(?P<language>[0-9]+)',
        ViewWrapper.as_view(view_func=doctor_view),
        name='doctor'),

    re_path(r'^doctor/(?P<category>[0-9]+)',
        ViewWrapper.as_view(view_func=doctor_view),
        name='doctor'),
    
    re_path(r'^doctor/(?P<fee>[0-9]\D)',
        ViewWrapper.as_view(view_func=doctor_view),
        name='doctor'),
    
    path('doctor',
        csrf_exempt(ViewWrapper.as_view(view_func=doctor_view)),
        name='doctor'),
]

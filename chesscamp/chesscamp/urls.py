"""
URL configuration for chesscamp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


# chess_platform/urls.py (Project URLs)

from django.contrib import admin
from django.urls import path, include
from chess import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chess.urls')),
    path('api/', include('forum.urls')),
    path('api/', include('notifications.urls')),
]


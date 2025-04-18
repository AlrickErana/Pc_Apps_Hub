from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns= [
    path('', views.home, name="home"),
    path('apps/', views.apps, name="apps"),
    path('games/', views.games, name="games"),
    path('about/', views.about, name="about"),
    path('all-apps/', views.all_apps_view, name='all_apps'),
    path('app/<int:id>/', views.app_detail, name='app_detail'),
    path('games/<int:id>/', views.game_detail, name='game_detail'),
    # path('contact/', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
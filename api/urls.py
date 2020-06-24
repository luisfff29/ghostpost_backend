from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'posts', views.GhostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/magic/<str:magic>/',
         views.GhostMagicView.as_view(), name='ghostmodel-detail')
]

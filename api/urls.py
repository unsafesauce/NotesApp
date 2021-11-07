from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import NoteViewSet, TaskViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('note', NoteViewSet)
router.register('task', TaskViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls))

]

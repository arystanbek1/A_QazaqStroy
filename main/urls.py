from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('obj', views.ObjectViewSet)


urlpatterns = [
    path('', views.regis, name='regis'),
    path('base/', views.base, name='base'),
    path('table/', views.table, name='table'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.ConcreteDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', views.ConcreteDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', views.ConcreteUpdateView.as_view(), name='update')


] + router.urls

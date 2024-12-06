from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'contributors', views.ContributorViewSet)
router.register(r'defis', views.DefisViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('contributors/<int:contributor_id>/defis/', views.get_contributor_defis, name='get_contributor_defis'),
    path('<str:defi_name>/total_montant/', views.total_montant_by_defi_name, name='total_montant_by_defi_name'),
    path('contributor/<int:contributor_id>/total_contribution/', views.total_contribution_by_contributor, name='total_contribution_by_contributor'),

]

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from .views import gestores_view, manutentores_view, patrimonios_view, ambientes_view

urlpatterns = [
    
    path('gestores', gestores_view.GestoresListCreateView.as_view()),
    path('gestores/id/<int:pk>', gestores_view.GestoresDetailView.as_view()),
    path('gestores/search/', gestores_view.GestoresSearchView.as_view()),

    path('manutentores', manutentores_view.ManutentoresListCreateView.as_view()),
    path('manutentores/id/<int:pk>', manutentores_view.ManutentoresDetailView.as_view()),
    path('manutentores/search/', manutentores_view.ManutentoresSearchView.as_view()),

    path('patrimonios', patrimonios_view.PatrimoniosListCreateView.as_view()),
    path('patrimonios/id/<int:pk>', patrimonios_view.PatrimoniosDetailView.as_view()),
    path('patrimonios/search/', patrimonios_view.PatrimoniosSearchView.as_view()),
]

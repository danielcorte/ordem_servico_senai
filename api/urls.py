from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
)

from .views import gestores_view, manutentores_view, patrimonios_view, ambientes_view, ordemservico_view, users_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('gestores', gestores_view.listar_gestores),
    path('gest', gestores_view.GestoresListCreateView.as_view()),
    path('gestores/id/<int:pk>', gestores_view.GestoresDetailView.as_view()),
    path('gestores/search', gestores_view.GestoresSearchView.as_view()),

    path('manutentores', manutentores_view.ManutentoresListCreateView.as_view()),
    path('manutentores/id/<int:pk>', manutentores_view.ManutentoresDetailView.as_view()),
    path('manutentores/search/', manutentores_view.ManutentoresSearchView.as_view()),

    path('patrimonios', patrimonios_view.PatrimoniosListCreateView.as_view()),
    path('patrimonios/id/<int:pk>', patrimonios_view.PatrimoniosDetailView.as_view()),
    path('patrimonios/search/', patrimonios_view.PatrimoniosSearchView.as_view()),

    path('ambientes', ambientes_view.AmbientesListCreateView.as_view()),
    path('ambientes/id/<int:pk>', ambientes_view.AmbientesDetailView.as_view()),
    path('ambientes/search/', ambientes_view.AmbientesSearchView.as_view()),

    path('ordemservico', ordemservico_view.OrdemServicoListCreateView.as_view()),
    path('ordemservico/id/<int:pk>', ordemservico_view.OrdemServicoDetailView.as_view()),
    path('ordemservico/search/', ordemservico_view.OrdemServicoSearchView.as_view()),

    path('registro', users_view.RegistroView.as_view(), name='registro'),
    path('usuario', users_view.UsuarioView.as_view(), name='usuario'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),


]

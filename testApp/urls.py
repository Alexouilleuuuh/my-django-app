from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import pca_cluste, pca_reduc, lda_reduc, graphe

from .Pages.home import test

urlpatterns = [
    path('', test),
    path('pca_cluster/', pca_cluste),
    path('sklearn_pca/', pca_reduc),
    path('sklearn_lda/', lda_reduc),
    path('graphe/', graphe),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
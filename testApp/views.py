from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .pca_clust import pca_clust
from .pca_reduc import pca_reduct
from .lda_reduc import lda_reduct

# Clustering des données avec K-means
def pca_cluste(request):
    return pca_clust(request)

# Réduction des données avec PCA 
def pca_reduc(request):
    return pca_reduct(request)

# Réduction des données avec LDA 
def lda_reduc(request):
    return lda_reduct(request)

# Apparition du graphe
def graphe(request):
    return render(request, 'graphe.html')

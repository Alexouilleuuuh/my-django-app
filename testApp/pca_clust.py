from django.shortcuts import render

import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import ColorPicker

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def pca_clust(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_file = request.FILES['file']
            data = pd.read_csv(data_file)
            pca = PCA(n_components=2)
            pca.fit(data)
            transformed_data = pca.transform(data)
            kmeans = KMeans(n_clusters=3)
            kmeans.fit(transformed_data)
            labels = kmeans.predict(transformed_data)
            # Création du graphe Bokeh
            x=transformed_data[:,0]
            y=transformed_data[:,1]
            
            TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,examine,help"
            p = figure(title="PCA Clustering", x_axis_label='x', y_axis_label='y',tools=TOOLS)
            scatter= p.scatter(x, y, legend_label="Cluster", size=10, fill_color='Blue')
            picker = ColorPicker(title="Color")
            picker.js_link('color', scatter.glyph, 'fill_color')

            output_file("testApp/templates/graphe.html")
            show(column(p, picker))

            context = {
                       'data': transformed_data,
                       'labels': labels
                    }
            return render(request, 'pca_results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'pca_form.html', {'form': form})

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    
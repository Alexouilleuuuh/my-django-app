import pandas as pd

from django.shortcuts import render

from sklearn.decomposition import PCA

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import ColorPicker

def pca_reduct(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                data_file = request.FILES['file']
                data = pd.read_csv(data_file)
                pca = PCA(n_components=2)
                reduced_data = pca.fit_transform(data)
                
                # Création du graphe Bokeh
                x = reduced_data[:, 0]
                y = reduced_data[:, 1]
                
                TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,examine,help"
                plot = figure(title="PCA reducing", x_axis_label='Composante 1', y_axis_label='Composante 2',tools=TOOLS)
                plot.scatter(x, y, legend_label="Réduction", size=10, fill_color='Blue')
                picker = ColorPicker(title="Color")
                scatter = picker.js_link('color', scatter.glyph, 'fill_color')
                output_file("testApp/templates/graphe.html")
                show(column(plot, picker))
                
                context = {
                       'data': data,
                       'labels': reduced_data
                    }
            return render(request, 'pca_results.html', context)
        else:
            form = UploadFileForm()
        return render(request, 'pca_form.html', {'form': form})

    
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
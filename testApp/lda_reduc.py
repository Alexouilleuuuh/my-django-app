import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import ColorPicker

from django.shortcuts import render

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA

def lda_reduct(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_file = request.FILES['file']
            data = pd.read_csv(data_file)
            data["c3"] = data["c3"].replace({"A": 0, "B": 1})
            pca = PCA(n_components=2)
            pca.fit(data)
            X = data.iloc[:, :-1].values
            y = data.iloc[:, -1].values
            lda = LinearDiscriminantAnalysis(n_components=2)
            lda.fit(X, y)
            X_reduced = lda.transform(X)
            # graphe Bokeh
            x = X_reduced[:, 0]
            y = X_reduced[:, 1]
            
            TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,examine,help"
            plot = figure(title="LDA reducing", x_axis_label='Composante 1', y_axis_label='Composante 2', tools=TOOLS)
            scatter = plot.scatter(x, y, legend_label="Réduction", size=10, fill_color='Blue')
            picker = ColorPicker(title="Color")
            picker.js_link('color', scatter.glyph, 'fill_color')
            output_file("testApp/templates/graphe.html")        
            show(column(plot, picker))
            
            return render(request, 'pca_results.html', {'data': X, 'labels': X_reduced})
    else:
        form = UploadFileForm()
    return render(request, 'pca_form.html', {'form': form})


from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
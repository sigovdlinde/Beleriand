from django.shortcuts import render, redirect
import folium
from folium.plugins import BeautifyIcon
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# circle marker
icon_circle = BeautifyIcon(
icon_shape='circle-dot',
border_color='red',
border_width=4,
)

# Create your views here.
@csrf_exempt
def post_form_api(request):
      data = {}
      if request.method == "POST":
          form_field1 = json.loads(request.body)
          # save the form data and indicate success
          data['result'] = True
          data['message'] = "Form saved successfully"
          print(form_field1)
      if request.is_ajax():
          return JsonResponse(data)
          # redirect('third', kwargs={ 'bar': FooBar })
      else:
          return HttpResponseBadRequest()

def home_view(request):

    context = {

    }

    return render(request, 'main.html', context)

def first_view(request):

    m = folium.Map(width='90%', height='90%', crs='Simple', tiles=None)
    image= 'static/images/Beleriand.jpg'
    bounds=[[0, 0], [200, 300]]

    folium.raster_layers.ImageOverlay(image, bounds).add_to(m)

    m.fit_bounds(bounds)

    m = m._repr_html_()

    context = {
        'map': m,
    }

    return render(request, 'first.html', context)

def second_view(request):

    m = folium.Map(width='90%', height='90%', crs='Simple', tiles=None)
    image= 'static/images/Second_Age.png'
    bounds=[[0, 0], [200, 300]]

    folium.raster_layers.ImageOverlay(image, bounds).add_to(m)

    m.fit_bounds(bounds)

    m = m._repr_html_()

    context = {
        'map': m,
    }

    return render(request, 'second.html', context)

@csrf_exempt
def third_view(request):
    last = None

    # if m is not None:
    #

    m = folium.Map(width='100%', height='90%', crs='Simple', tiles=None)
    base_map = folium.FeatureGroup(name='Basemap')

    image= 'static/images/stitched_map.png'
    bounds=[[0, 0], [750, 750]]

    overlay = folium.raster_layers.ImageOverlay(image, bounds).add_to(base_map)
    base_map.add_to(m)

    html = 'Here lies Balin, son of Fundin'

    iframe = folium.IFrame(html)
    popup = folium.Popup(iframe,
                         min_width=200,
                         max_width=200)

    layer1 = folium.FeatureGroup(name='layer1', show=False)
    folium.Marker([350, 350], icon=icon_circle, tooltip='TA 1267', popup=popup).add_to(layer1)
    if request.method == "POST":
        print('poep')
        layer1.add_to(m)

        m.fit_bounds(bounds)
        m = m._repr_html_()


        context = {
            'map': m,
        }

        return JsonResponse(context)

    m.fit_bounds(bounds)
    m = m._repr_html_()


    context = {
        'map': m,
    }

    return render(request, 'third.html', context)

def fourth_view(request):

    context = {

    }

    return render(request, 'fourth.html', context)

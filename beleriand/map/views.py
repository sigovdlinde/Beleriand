from django.shortcuts import render
import folium
from folium.plugins import BeautifyIcon

# Create your views here.
def home_view(request):


    m = folium.Map(width='90%', height='90%', crs='Simple', tiles=None)
    image= 'static/images/stitched_map.png'
    bounds=[[0, 0], [900, 900]]

    overlay = folium.raster_layers.ImageOverlay(image, bounds)
    overlay.add_to(m)

    # circle marker
    icon_circle = BeautifyIcon(
    icon_shape='circle-dot',
    border_color='green',
    border_width=4,
    )
    folium.Marker([350, 350], tooltip='circle', icon=icon_circle).add_to(m)

    m.fit_bounds(bounds)

    m = m._repr_html_()

    context = {
        'map': m,
    }

    return render(request, 'main.html', context)

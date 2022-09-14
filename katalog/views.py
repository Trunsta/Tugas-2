from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'katalog_item' : data_catalog_item,
        'nama' : 'Nikolas Reva Bellie',
        'NPM' : '2106750212'
    }
    return render(request, "katalog.html", context)

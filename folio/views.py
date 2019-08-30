from django.shortcuts import render, get_object_or_404
from .models import Folio

# Create your views here.
def home(request):
    folios = Folio.objects.all()
    context = {'folios': folios}
    return render(request, "folio/index.html", context)

def foliodetail(request, folio_id):
    folio = get_object_or_404(Folio, pk=folio_id)
    context = {'folio': folio}
    return render(request, "folio/folio_detail.html", context)
from django.shortcuts import render
from django.http import HttpResponse
from top_movers.models import get_topmovers
# Create your views here.

def top_movers( request):

    all_movers = get_topmovers.objects.all



    return render(request, 'top_m.html', {'all_movers': all_movers})

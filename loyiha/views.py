from django.shortcuts import render
from loyiha.models import Loyiha


def ProjectList(request):
    loyiha = Loyiha.objects.all().order_by('-created_at')

    context = {
        'loyiha': loyiha,
    }
    return render(request, 'loyiha/loyiha.html', context)

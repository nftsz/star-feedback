from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Avg
from django.http import JsonResponse

# Create your views here.
def lista_roms(request):
    roms = ROM.objects.all().annotate(media=Avg('avaliacoes__estrelas'))
    
    return render(request, '', {'roms': roms}) # LEMBRETE: adicionar o HTML

def avaliar_rom(request, rom_id):
    rom = get_object_or_404(ROM, id=rom_id)
    if request.method == 'POST':
        estrelas = int(request.POST.get('estrelas', 0))
        if 1 <= estrelas <= 5:
            Avaliacao.objects.create(rom=rom, estrelas=estrelas)
            media = rom.avaliacoes.aggregate(models.Avg('estrelas'))['estrelas__avg']
            return JsonResponse({'media': media})
    return JsonResponse({'erro': 'Dados inválidos'}, status=400)

from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Avg
from django.http import JsonResponse

# Create your views here.
def lista_roms(request):
    roms = ROM.objects.all().annotate(media=Avg('avaliacoes__estrelas'))
    
    return render(request, 'core/lista.html', {'roms': roms}) # LEMBRETE: adicionar o HTML


def avaliar_rom(request, rom_id):
    rom = get_object_or_404(ROM, id=rom_id)
    session_id = request.session.session_key or request.session.create()

    if request.method == 'POST':
        estrelas = int(request.POST.get('estrelas', 0))
        if 1 <= estrelas <= 5:
            avaliacao, created = Avaliacao.objects.update_or_create(
                rom=rom, session_id=session_id,
                defaults={'estrelas': estrelas}
            )
            media = rom.avaliacoes.aggregate(media=Avg('estrelas'))['media']
            return JsonResponse({'media': round(media, 2), 'nova': created})
    return JsonResponse({'erro': 'Dados inválidos'}, status=400)

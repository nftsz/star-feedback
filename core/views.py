from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Avg
from django.http import JsonResponse

# Create your views here.
def lista_roms(request):
    # pega todas as ROMs e adiciona um campo 'media' com a média das avaliações
    roms = ROM.objects.all().annotate(media=Avg('avaliacoes__estrelas'))
    # Renderiza o template passando as ROMs com suas médias
    return render(request, 'core/home.html', {'roms': roms}) 


def avaliar_rom(request, rom_id):
    # pega a ROM pelo ID ou retorna 404 se não existir
    rom = get_object_or_404(ROM, id=rom_id)
    # garante que a sessão do usuário exista
    session_id = request.session.session_key or request.session.create()

    if request.method == 'POST':
        estrelas = int(request.POST.get('estrelas', 0))
        if 1 <= estrelas <= 5:
            avaliacao, created = Avaliacao.objects.update_or_create(
                rom=rom, session_id=session_id,
                defaults={'estrelas': estrelas}
            )
            # calcula a média atualizada das estrelas da ROM
            media = rom.avaliacoes.aggregate(media=Avg('estrelas'))['media']
            # retorna a média e se foi criação ou atualização
            return JsonResponse({'media': round(media, 2), 'nova': created})
    return JsonResponse({'erro': 'Dados inválidos'}, status=400)

def detalhe_rom(request, rom_id):
    rom = get_object_or_404(ROM, id=rom_id)
    return render(request, "core/detalhe_rom.html", {"rom": rom})
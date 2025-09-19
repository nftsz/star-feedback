from django.shortcuts import render, get_object_or_404
from .models import ROM, Avaliacao
from django.db.models import Avg, Value
from django.http import JsonResponse
from django.db.models.functions import Coalesce
from django.db.models import FloatField


def lista_roms(request):
    # pega todas as ROMs com média de avaliação e pré-carrega imagens relacionadas
    roms = (ROM.objects
        .all()
        .annotate(media=Coalesce(Avg('avaliacoes__estrelas'), Value(0, output_field=FloatField())))
        .prefetch_related('imagens')
        .order_by('-media')[:5])
    roms_recent = (ROM.objects.all().annotate(media=Avg('avaliacoes__estrelas')).prefetch_related('imagens').order_by('-criado_em')[:5])

    # transforma a média em int arredondado pra facilitar mostrar estrelas
    for rom in roms:
        rom.media_int = int(round(rom.media or 0))
    for rom in roms_recent:
        rom.media_int = int(round(rom.media or 0))

    return render(request, 'core/home.html', {'roms': roms, 'roms_recent': roms_recent})

def avaliar_rom(request, rom_id):
    rom = get_object_or_404(ROM, id=rom_id)

    # garante session_key única
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    if request.method == 'POST':
        try:
            estrelas = int(request.POST.get('estrelas', 0))
        except ValueError:
            return JsonResponse({'erro': 'Estrelas inválidas'}, status=400)

        if 1 <= estrelas <= 5:
            avaliacao, created = Avaliacao.objects.update_or_create(
                rom=rom,
                session_id=session_id,
                defaults={'estrelas': estrelas}
            )
            media = rom.avaliacoes.aggregate(media=Avg('estrelas'))['media']
            return JsonResponse({'media': round(media, 2), 'nova': created})
        
    return JsonResponse({'erro': 'Dados inválidos'}, status=400)

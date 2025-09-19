from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# função para criar pastas por ROM
def rom_jogo_path(instance, filename):
    # tira espaços e caracteres problemáticos
    nome_rom = instance.rom.nome.replace(" ", "_").lower()
    return f'roms_jogo/{nome_rom}/{filename}'

# Create your models here.
class ROM(models.Model):
    EMULADOR_CHOICES =   [
        ('nswitch', 'Nintendo Switch'),
        ('gba', 'GBA'),
        ('nes', 'NES'),
        ('ps1', 'PS1'),
        ('ps2', 'PS2'),
        ('ps3', 'PS3'),
    ]

    nome = models.CharField(max_length=100)
    emulador = models.CharField(max_length=10, choices=EMULADOR_CHOICES)
    imagem_capa = models.ImageField(upload_to='roms_capa/', default="default.jpg")
    estudio = models.CharField(max_length=100, blank=True)
    sinopse = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.get_emulador_display()})"
    
class ImagemJogo(models.Model):
    rom = models.ForeignKey(ROM, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to=rom_jogo_path)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Imagem de {self.rom.nome} - {self.descricao or 'sem descrição'}"

# função pra gerar session_id único
def gerar_session_id():
    return str(uuid.uuid4())
    
class Avaliacao(models.Model):
    rom = models.ForeignKey(ROM, on_delete=models.CASCADE, related_name='avaliacoes')
    estrelas = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # identifica a sessão do usuário (não precisa logar)
    session_id = models.CharField(max_length=40, default=gerar_session_id)
    criado_em = models.DateTimeField(auto_now_add=True)

    # faz com que cada sessão só possa avaliar a mesma ROM uma vez
    class Meta:
        unique_together = ('rom', 'session_id')  
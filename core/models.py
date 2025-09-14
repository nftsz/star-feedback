from django.db import models

# Create your models here.
class ROM(models.Model):
    EMULADOR_CHOICES =   [
        ('nswitch', 'Nintendo Switch'),
        ('gba', 'Game Boy Advance'),
        ('nes', 'NES'),
        ('ps1', 'PS1'),
        ('ps2', 'PS2'),
        ('ps3', 'PS3'),
    ]

    nome = models.CharField(max_length=100)
    emulador = models.CharField(max_length=10, choices=EMULADOR_CHOICES)
    imagem = models.ImageField(upload_to='roms/')

    def __str__(self):
        return f"{self.nome} ({self.get_emulador_display()})"
    
class Avaliacao(models.Model):
    rom = models.ForeignKey(ROM, on_delete=models.CASCADE, related_name='avaliacoes')
    estrelas = models.PositiveBigIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
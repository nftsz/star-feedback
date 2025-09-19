from django.db import models

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
    imagem = models.ImageField(upload_to='roms/')
    # data de entrada da ROM, para listagem no "recentes adicionados"

    def __str__(self):
        return f"{self.nome} ({self.get_emulador_display()})"
    
class Avaliacao(models.Model):
    rom = models.ForeignKey(ROM, on_delete=models.CASCADE, related_name='avaliacoes')
    estrelas = models.PositiveBigIntegerField()
    # identifica a sessão do usuário (não precisa logar)
    session_id = models.CharField(max_length=40, default="anon")
    criado_em = models.DateTimeField(auto_now_add=True)

    # faz com que cada sessão só possa avaliar a mesma ROM uma vez
    class Meta:
        unique_together = ('rom', 'session_id')  
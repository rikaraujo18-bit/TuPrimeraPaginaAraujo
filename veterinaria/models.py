from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    ESPECIES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('conejo', 'Conejo'),
        ('ave', 'Ave'),
        ('otro', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    edad = models.IntegerField()
    dueno = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')
    
    def __str__(self):
        return f"{self.nombre} ({self.dueno.nombre})"

class Consulta(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='consultas')
    fecha = models.DateField(auto_now_add=True)
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Consulta de {self.mascota.nombre} - {self.fecha}"
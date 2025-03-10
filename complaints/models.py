from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('resuelto', 'Resuelto'),
        ('rechazado', 'Rechazado'),
    ]

    CATEGORY_CHOICES = [
        ('mantenimiento', 'Mantenimiento'),
        ('ruido', 'Ruido'),
        ('seguridad', 'Seguridad'),
        ('limpieza', 'Limpieza'),
        ('areas_comunes', 'Áreas comunes'),
        ('recepcion', 'Recepcion'),
        ('mascotas', 'Mascotas'),
        ('desastres_naturales', 'Desastres Naturales'),
        ('olores', 'Olores Desagradables'),
        ('otro', 'Otro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The resident submitting the complaint
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', blank=True, null=True) 
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='otro')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


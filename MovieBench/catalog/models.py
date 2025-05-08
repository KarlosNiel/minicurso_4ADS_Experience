from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
    
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 

    objects = SoftDeleteManager()
    all_objects =  models.Manager()

    class Meta:
        abstract = True 

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
    
    def hard_delete(self):
        super().delete()

    def restore(self):
        self.deleted_at = None
        self.save()

class Genre(BaseModel):
    name = models.CharField(max_length=255, unique=True)  # Nome único para evitar duplicatas

    def __str__(self):
        return self.name
    
class Person(BaseModel):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)  # Opcional
    description = models.TextField(null=True, blank=True)  # Opcional

    def __str__(self):
        return self.name
    
class Streaming(BaseModel):
    name = models.CharField(max_length=255)
    website = models.URLField()  # URL válida

    def __str__(self):
        return self.name
    
class Movie(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(null=True, blank=True)  # Duração em minutos (opcional)
    imdb_rating = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]  # Nota entre 0 e 10
    )
    poster_url = models.URLField(null=True, blank=True)  # URL do pôster (opcional)
    genres = models.ManyToManyField(Genre, related_name='movies')  # Gêneros do filme
    director = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,  # Diretor pode ser nulo se excluído
        null=True, blank=True,
        related_name='directed_movies'
    )
    actors = models.ManyToManyField(Person, related_name='acted_movies')  # Atores
    streaming = models.ManyToManyField(Streaming, related_name='movies')  # Plataformas

    def __str__(self):
        return self.title
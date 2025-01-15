from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
from django.conf import settings


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f"media/{filename}"
class Snack(models.Model):
    type_choices = (
        ("almoço", "almoço"),
        ("janta", "janta"),
    )
    description = models.TextField("Descrição", max_length=255)
    likes = models.IntegerField("Curtidas", default=0, null=True, blank=True)
    image = models.ImageField("Imagem", upload_to=get_file_path, null=True)
    snack_to_day = models.BooleanField("Refeição do dia", default=False)
    type = models.CharField("Tipo", max_length=15, choices=type_choices)
    active = models.BooleanField("Ativo", default=True, null=True, blank=True)

    class Meta:
        verbose_name = "Refeição"

class RequestSnack(models.Model):
    snack_types = Snack.type_choices
    snack_status = (
        ("aprovado", "aprovado"),
        ("reprovado", "reprovado"),
        ("pendente", "pendente"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuário", default=1)
    data = models.DateField("Data")
    justification = models.TextField("Justificativa", max_length=300)
    status = models.CharField("Situação", blank=True, null=True, choices=snack_status, default="pendente", max_length=15)
    type = models.CharField("Tipo", max_length=15, choices=snack_types)
    checked = models.BooleanField("Verificado", default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Solicitação de Refeição"


class CustomUser(AbstractUser):
    is_holder = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
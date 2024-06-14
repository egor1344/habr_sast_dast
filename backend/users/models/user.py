from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователь."""

    class Meta:
        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"

    def __str__(self) -> str:
        return f"{self.username}"

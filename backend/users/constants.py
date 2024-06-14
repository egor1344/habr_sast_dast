from django.db.models import TextChoices


class SexChoice(TextChoices):

    """Выбор пола."""

    MALE = "male", "мужской"
    FEMALE = "female", "женский"


OTP_TOKEN_VALIDATION_TIME = 2
OTP_TOKEN_USE_TIME = 30
OTP_TOKEN_MAX_RETRY = 10


class OTPTokenType(TextChoices):

    """Тип выдачи OTP токена."""

    LOGIN = "login", "Вход в личный кабинет"
    BOOKING = "booking", "Подтверждение бронирования"

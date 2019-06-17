from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (('', '----'), ('1', ('Estudante')),
            ('2', ('Corpo docente')), ('3', ('Funcionários')))

ENGINEERING = (('0', '----'), ('1', ('Software')), ('2', ('Eletrônica')),
               ('3', ('Energia')), ('4', ('Automotivo')),
               ('5', ('Aeroespacial')), ('6', ('Engenharia')))


class UserProfile(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    category = models.CharField(choices=CATEGORY, max_length=20)
    engineering = models.CharField(choices=ENGINEERING, max_length=15, default=1)


class Settings(models.Model):
    start_semester = models.DateField(null=False, blank=False)
    end_semester = models.DateField(null=False, blank=False)

    def get_start(self):
        return Settings.objects.last().start_semester

    def get_end(self):
        return Settings.objects.last().end_semester


class Validation():
    def hasNumbers(self, string):
        if (string is not None):
            if any(char.isdigit() for char in string):
                return True

            return False

        else:
            return False

    def hasLetters(self, number):
        if (number is not None):
            if any(char.isalpha() for char in number):
                return True

            return False

        else:
            return False

    def hasSpecialCharacters(self, string):
        if (string is not None):
            for character in '@#$%^&+=/\{[]()}-_+=*!§|':
                if character in string:
                    return True

        return False
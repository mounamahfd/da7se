from django.db import models


class Contributor(models.Model):
    SPECIALITE_CHOICES = [
        ('frontend', 'Développeur Front-end'),
        ('backend', 'Développeur Back-end'),
        ('fullstack', 'Développeur Full-stack'),
        ('uiux', 'Designer UI/UX'),
        ('devops', 'Ingénieur DevOps'),
        ('data', 'Scientifique de Données'),
        ('pm', 'Chef de Projet'),
    ]

    name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100, unique=True)
    avatar_url = models.URLField()
    specialite = models.CharField(
        max_length=100,
        choices=SPECIALITE_CHOICES,
        default='fullstack'
    )


    def __str__(self):
        return self.name

class Defis(models.Model):
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE,
        related_name="defis"
    )
    nom_du_defis = models.CharField(max_length=200)
    montant = models.IntegerField()  # New montant attribute

    def __str__(self):
        return f"{self.nom_du_defis} - {self.montant} units"

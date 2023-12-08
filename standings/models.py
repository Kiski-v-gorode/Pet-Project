from django.db import models

# Create your models here.


class Team(models.Model):
    id_team = models.IntegerField(unique=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


class Match(models.Model):
    tour = models.IntegerField()
    date = models.IntegerField()
    owner_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches', to_field="id_team")
    guest_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches', to_field="id_team")
    owner_goals = models.IntegerField()
    guest_goals = models.IntegerField()
    is_over = models.BooleanField()

    def __str__(self):
        return f"{self.owner_id.name} - {self.guest_id.name}"


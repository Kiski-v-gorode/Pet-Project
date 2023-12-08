from rest_framework import serializers
from .models import Team, Match


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id_team', 'name']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ["owner_id", "guest_id", "owner_goals", "guest_goals"]


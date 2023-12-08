from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from .general import generate_standings


class StandingsView(APIView):
    def get(self, request):
        teams = models.Team.objects.all()
        matches = models.Match.objects.filter(is_over=True)

        teams_serializer = serializers.TeamSerializer(teams, many=True)
        matches_serializer = serializers.MatchSerializer(matches, many=True)

        response = generate_standings(teams_serializer.data, matches_serializer.data)

        return Response(response)

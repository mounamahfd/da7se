from rest_framework import serializers
from .models import Contributor ,Defis

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'name', 'github_username', 'avatar_url', 'specialite']

    def get_total_contributions(self, obj):
        return sum(defi.montant for defi in obj.defis.all())


class DefisSerializer(serializers.ModelSerializer):
    contributor_name = serializers.ReadOnlyField(source='contributor.name')  # Optional: To display the contributor's name
    class Meta:
        model = Defis
        fields = '__all__'
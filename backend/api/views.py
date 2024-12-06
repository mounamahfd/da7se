from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Contributor,Defis
from .serializers import ContributorSerializer,DefisSerializer


from rest_framework.viewsets import ModelViewSet



from django.db.models import Sum
class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

class DefisViewSet(viewsets.ModelViewSet):
    queryset = Defis.objects.all()
    serializer_class = DefisSerializer

@api_view(['GET'])
def get_contributor_defis(request, contributor_id):
    try:
        contributor = Contributor.objects.get(id=contributor_id)
        defis = contributor.defis.all()  
        return Response({'defis': [defi.name for defi in defis]})
    except Contributor.DoesNotExist:
        return Response({'error': 'Contributor not found'}, status=404)

    return Response(defis_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_montant_by_defi_name(request, defi_name):
    total_montant = Defis.objects.filter(nom_du_defis=defi_name).aggregate(
        total=Sum('montant')
    )['total'] or 0
    return Response({"total_montant": total_montant}, status=status.HTTP_200_OK)



@api_view(['GET'])
def total_contribution_by_contributor(request, contributor_id):

    total_contribution = Defis.objects.filter(contributor_id=contributor_id).aggregate(
        total=Sum('montant')
    )['total'] or 0

    return Response(
        {"total_contribution": total_contribution},
        status=status.HTTP_200_OK
    )

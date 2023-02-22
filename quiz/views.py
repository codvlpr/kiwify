from django.db import transaction

from rest_framework import viewsets
from rest_framework.response import Response

from quiz.models import MetaData
from quiz.serializers import MetaDataSerializer

class QuizViewSet(viewsets.ViewSet):

    def list(self, request):
        metadata = MetaData.objects.prefetch_related('question_set__answer_set').all()
        serializer = MetaDataSerializer(metadata, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        metadata = MetaData.objects.prefetch_related('question_set__answer_set').get(pk=pk)
        serializer = MetaDataSerializer(metadata)
        return Response(serializer.data)
    
    @transaction.atomic
    def create(self, request):
        serializer = MetaDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

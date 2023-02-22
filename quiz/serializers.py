from rest_framework import serializers

from .models import MetaData, Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['reply', 'rightAnswer']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, source='answer_set')

    class Meta:
        model = Question
        fields = ['title', 'description', 'mandatory', 'answers']

class MetaDataSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = MetaData
        fields = ['title', 'description', 'published', 'questions']
    
    def create(self, validated_data):
        print(validated_data)
        questions_data = validated_data.pop('question_set')
        metadata = MetaData.objects.create(**validated_data)
        for question_data in questions_data:
            answers_data = question_data.pop('answer_set')
            question = Question.objects.create(metaDataId=metadata, **question_data)
            for answer_data in answers_data:
                Answer.objects.create(questionId=question, **answer_data)
        return metadata
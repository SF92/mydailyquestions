from rest_framework import serializers
from rest_framework import exceptions

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "question_text")

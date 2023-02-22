""" Includes every endpoint for the quiz app """
from rest_framework import routers

from quiz.views import QuizViewSet

router = routers.DefaultRouter()
router.register(r'', QuizViewSet, basename='quiz')

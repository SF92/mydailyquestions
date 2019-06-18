from django.conf.urls import url
from q_and_a import views
from django.conf.urls import url, include

# TEMPLATE TAGGING
app_name = "q_and_a"

urlpatterns = [
    url("Question/", views.Question.as_view(), name="Question"),
    url("Answer/", views.Answer.as_view(), name="Answer"),
]


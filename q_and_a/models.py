from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    is_active = models.BooleanField(default=True)

    # Link to user account
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Info Fields
    question_text = models.CharField(max_length=512)

    def __str__(self):
        return self.question_text[0:40]


class Answer(models.Model):

    is_active = models.BooleanField(default=True)

    # Link to Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Link to user account
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Info Fields
    answer_text = models.CharField(max_length=1024)
    answer_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            str(self.user)
            + "'s Answer to '"
            + self.question.question_text[0:40]
            + "' on "
            + str(self.answer_date)
        )


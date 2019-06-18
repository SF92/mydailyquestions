from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from q_and_a.models import Question as Question_Model, Answer as Answer_Model


from .serializers import QuestionSerializer


class Question(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):

        user = request.user
        question_text = request.data["question_text"]

        if Question_Model.objects.filter(
            user=user, question_text=question_text, is_active=True
        ):
            msg = "This question already exists"
            return Response(msg, status=400)

        else:
            new_Question = Question_Model(user=user, question_text=question_text)
            new_Question.save()
            return Response(status=200)

    def get(self, request):

        user = request.user

        question_response = Question_Model.objects.filter(user=user, is_active=True)

        serialized_response = QuestionSerializer(question_response, many=True).data
        return Response(serialized_response, status=200)


class Answer(APIView):
    def post(self, request):
        authentication_classes = (TokenAuthentication,)

        user = request.user
        answer_text = request.data["answer_text"]
        question_id = request.data["question_id"]

        print("answer_text = ", answer_text)
        print("question_id = ", question_id)

        # Get question_object:
        try:
            answered_question = Question_Model.objects.get(id=question_id, user=user)
        except Question_Model.DoesNotExist:
            msg = "Could not find question in database"
            return Response(msg, status=400)

        # Save new Answer:
        new_Answer = Answer_Model(
            user=user, question=answered_question, answer_text=answer_text
        )
        new_Answer.save()

        print(new_Answer)

        return Response(status=200)


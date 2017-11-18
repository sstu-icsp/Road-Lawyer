from rest_framework.decorators import api_view
from rest_framework.response import Response

from dialog_manager.services import save_user_message, simple_classifier


@api_view(['get'])
def get_answer(request):
    """
    Функция представляет сообой рест апи для получения ответов на вопрос пользователя
    :param request: Вставляется автоматически фреймворком django-rest-framework
    :return: Возвращеет список ответов пользователя
    """
    text = request.query_params['text']
    chat_id = request.query_params['chat_id']
    save_user_message(chat_id=chat_id, text=text)
    responses = simple_classifier(chat_id, text)
    result_responses = []
    for response in responses:
        result_responses.append({"text": response.text})

    return Response(result_responses)

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response.data['detail'].code == 'not_authenticated':
        response.data['detail'] = ('Не авторизованным пользователям'
                                   ' не доступен функционал подписок!')
    return response

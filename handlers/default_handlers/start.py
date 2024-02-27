from keyboards.inline.button import keyboard_commands
from telebot.types import Message, CallbackQuery

from loader import bot


@bot.message_handler(commands=["start", "help", "lowprice", "highprice", "bestdeal", "history"])
def start_command(message: Message) -> None:
    """
    Функция - обработчик сообщений. Реагирует на команды из списка 'COMMAND'.
    Исходя из пойманной команды, отправляет пользователя в соответствующий сценарий.
    Первым делом, очищает экземпляр класса UserHandle,
    так как с данного места берут начало новые команды.

    :param message: Message
    :return: None
    """
    if message.text == '/start':
        bot.send_message(message.from_user.id, f"👋Привет, {message.from_user.first_name}!\n"
                                               f"Добро пожаловать в телеграм-бот турагентства по поиску отелей -\n"
                                               f"<b>Too Easy Travel</b>", parse_mode="html")
        bot.send_message(
            message.from_user.id, "Нажмите кнопку 'Help'", reply_markup=keyboard_commands(message.text)
        )

    elif message.text == '/help':
        bot.send_message(
            message.from_user.id, '/lowprice -  вывод самых дешёвых отелей в городе\n'
                                  '/highprice - вывод самых дорогих отелей в городе\n'
                                  '/bestdeal -  вывод отелей, наиболее подходящих по цене и расположению от центра\n'
                                  '/history - вывод истории поиска отелей',
            reply_markup=keyboard_commands(message.text))


@bot.callback_query_handler(func=lambda call: call.data.startswith('/'))
def callback_command(call: CallbackQuery) -> None:
    """
        Функция - обработчик inline-кнопок. Реагирует только на команды.
        Исходя из пойманной команды, отправляет пользователя в соответствующий сценарий.
        Первым делом, очищает экземпляр класса UserHandle,
        так как с данного места берут начало новые команды.

        :param call: CallbackQuery
        :return: None
        """

    if call.data == '/help':
        bot.send_message(
            call.from_user.id, '<b>/lowprice</b> -  Вывод самых дешёвых отелей в городе\n'
                               '<b>/highprice</b> - Вывод самых дорогих отелей в городе\n'
                               '<b>/bestdeal</b> -  Вывод отелей, наиболее подходящих по цене и расположению от центра\n'
                               '<b>/history</b> - Вывод истории поиска отелей',
            parse_mode="html"
        )

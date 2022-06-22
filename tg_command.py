from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, ConversationHandler
import controller
from main import telephone_directory


ADD_KEY = range(1)


def start_main_menu(update: Update, _):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}, перед тобой телефонный справочник.\n'
                               'Хочешь увидеть функционал или сразу приступим к работе?\n'
                               'Ответь "хочу" или нажми любую клавишу')


def start_add(update: Update, _):
    update.message.reply_text('Введи индекс контакта')
    return ADD_KEY


def add_key(update: Update, _):
    key = update.message.text.split()
    controller.add_data_telephone(key[0], telephone_directory, key[1])
    print(telephone_directory)
    return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.'
    )
    return ConversationHandler.END


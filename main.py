from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler
import controller

telephone_directory = {}

ADD_KEY, ADD_DATA = range(2)
EDIT_KEY, EDIT_DATA = range(2)
DELETE_KEY = range(1)
key = ''


def start_main_menu(update: Update, _):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}, перед тобой телефонный справочник.\n'
                               'Вот, что я умею:\n'
                               '"/add" - добавить контакт в справочник\n'
                               '"/edit" - редактировать ранее добавленный контакт\n'
                               '"/delete" - удалить указанный контакт\n'
                               '"/cls" - очистить весь справочник\n'
                               '"/print" - напечатать справочник в консоль\n'                        
                               '"/print_in_file" - выгрузить справочник в файл в указанном формате\n'
                               '"/load_on_file" - добавить в справочник данные из файла\n'
                               '"/exit" - закрыть справочник(сохранение в файл "txt_line")\n'
                               'Приступим? Введи команду')


def add_start(update: Update, _):
    update.message.reply_text('Введи индекс контакта')
    update.message.reply_text('Для выхода введи /cancel\nВозврат в главное меню - /start')
    return ADD_KEY


def add_key(update: Update, _):
    global key
    key = update.message.text
    update.message.reply_text('Введи данные контакта')
    update.message.reply_text('Для выхода введи /cancel\nВозврат в главное меню - /start')
    return ADD_DATA


def add_data(update: Update, _):
    update.message.reply_text('Для отмены введи /cancel\nВозврат в главное меню - /start')
    data = update.message.text
    controller.add_data_telephone(key, telephone_directory, data)
    update.message.reply_text('Данные добавлены')
    print(telephone_directory)
    return ConversationHandler.END


def edit_start(update: Update, _):
    update.message.reply_text('Введи индекс контакта для редактирования')
    update.message.reply_text('Для выхода введи /cancel\nВозврат в главное меню - /start')
    return EDIT_KEY


def edit_key(update: Update, _):
    global key
    key = update.message.text
    update.message.reply_text('Введи, строку формата "(дата, номер, ФИО или комментрарий)/новые данные"')
    update.message.reply_text('Для выхода введи /cancel\nВозврат в главное меню - /start')
    return EDIT_DATA


def edit_data(update: Update, _):
    update.message.reply_text('Для выхода введи /cancel\nВозврат в главное меню - /start')
    data = update.message.text.split('/')
    controller.edit_data_tel(key, data[1], telephone_directory, data[0])
    update.message.reply_text('Данные отредактированы')
    print(telephone_directory)
    return ConversationHandler.END


def delete_start(update: Update, _):
    update.message.reply_text('Введи индекс контакта, который необходимо удалить')
    update.message.reply_text('Для выхода введи /cancel\nВозврат в главное меню - /start')
    return DELETE_KEY


def delete(update: Update, _):
    global key
    key = update.message.text
    controller.del_data_tel(key, telephone_directory)
    update.message.reply_text('Контакт удалён')
    return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться\n'
        'Будут нужны номера - пиши.\n'
        '/start'
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater('5375496557:AAGzB-SB1rey_oojdTnggtOGUxOX9uL6TBs')
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start_main_menu)
    add_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_start)],
        states={
            ADD_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), add_key)],
            ADD_DATA: [MessageHandler(filters.Filters.text & (~filters.Filters.command), add_data)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    edit_handler = ConversationHandler(
        entry_points=[CommandHandler('edit', edit_start)],
        states={
            EDIT_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), edit_key)],
            EDIT_DATA: [MessageHandler(filters.Filters.text & (~filters.Filters.command), edit_data)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(add_handler)
    dispatcher.add_handler(edit_handler)

    updater.start_polling()
    updater.idle()

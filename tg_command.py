from telegram import Update
from telegram.ext import  ConversationHandler
import controller
from main import telephone_directory


ADD_KEY, ADD_DATA = range(2)
EDIT_KEY, EDIT_DATA = range(2)
DELETE_KEY = range(1)
CLS_KEY = range(1)
PRINT_KEY = range(1)
PRINT_FILE_KEY = range(1)

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
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return ADD_KEY


def add_key(update: Update, _):
    global key
    key = update.message.text
    update.message.reply_text('Введи данные контакта в формате ФИО/номер телефона/комментарий')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return ADD_DATA


def add_data(update: Update, _):
    data = update.message.text
    controller.add_data_telephone(key, telephone_directory, data)
    update.message.reply_text('Данные добавлены')
    update.message.reply_text('Для отмены введи /exit\nВозврат в главное меню - /start')
    print(telephone_directory)
    return ConversationHandler.END


def edit_start(update: Update, _):
    update.message.reply_text('Введи индекс контакта для редактирования')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return EDIT_KEY


def edit_key(update: Update, _):
    global key
    key = update.message.text
    update.message.reply_text('Введи, строку формата "(дата, номер, ФИО или комментрарий)/новые данные"')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return EDIT_DATA


def edit_data(update: Update, _):
    data = update.message.text.split('/')
    controller.edit_data_tel(key, data[1], telephone_directory, data[0])
    update.message.reply_text('Данные отредактированы')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    print(telephone_directory)
    return ConversationHandler.END


def delete_start(update: Update, _):
    update.message.reply_text('Введи индекс контакта, который необходимо удалить')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return DELETE_KEY


def delete(update: Update, _):
    global key
    key = update.message.text
    controller.del_data_tel(key, telephone_directory)
    update.message.reply_text('Контакт удалён')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return ConversationHandler.END


def cls_start(update: Update, _):
    update.message.reply_text('Справочник автоматически очистится при закрытии бота\n'
                              'Ты уверен, что хочешь сделать это сейчас?\n Введи "да"')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return CLS_KEY


def cls(update: Update, _):
    global key
    key = update.message.text
    if key == 'да' or key == 'Да':
        controller.del_all_data_tel(telephone_directory)
        update.message.reply_text('Справочник успешно очищен')
        update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
        return ConversationHandler.END


def print_start(update: Update, _):
    update.message.reply_text('Введи индекс контакта для печати в консоль или all для печати всего справочника')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return PRINT_KEY


def print_directory(update: Update, _):
    global key
    key = update.message.text
    update.message.reply_text(f'Внесённые данные\n{controller.print_string_directory(key, telephone_directory)}')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return ConversationHandler.END


def print_in_file_start(update: Update, _):
    update.message.reply_text('Укажи необходимый формат: json ||  txt_line ||  txt_columns')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')
    return PRINT_FILE_KEY


def print_in_file(update: Update, _):
    global key
    key = update.message.text
    controller.print_in_file(telephone_directory, key)
    update.message.reply_document('file://С9/data_dictionary_line.txt')
    update.message.reply_text('Для выхода введи /exit\nВозврат в главное меню - /start')


def cancel_exit(update, _):
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться\n'
        'Будут нужны номера - пиши.\n'
        '/start'
    )
    controller.print_in_file(telephone_directory, 'txt_line')
    return ConversationHandler.END


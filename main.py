from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler

import logger_t
from logger_t import logger_cls
import tg_command


telephone_directory = {}

if __name__ == '__main__':
    logger_cls()
    logger_t.logger.info('Start bot')
    updater = Updater('5375496557:AAGzB-SB1rey_oojdTnggtOGUxOX9uL6TBs')
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', tg_command.start_main_menu)
    end_handler = CommandHandler('exit', tg_command.cancel_exit)
    add_handler = ConversationHandler(
        entry_points=[CommandHandler('add', tg_command.add_start)],
        states={
            tg_command.ADD_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.add_key)],
            tg_command.ADD_DATA: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.add_data)]
        },
        fallbacks=[CommandHandler('exit', tg_command.cancel_exit)]
    )
    edit_handler = ConversationHandler(
        entry_points=[CommandHandler('edit', tg_command.edit_start)],
        states={
            tg_command.EDIT_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.edit_key)],
            tg_command.EDIT_DATA: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.edit_data)]
        },
        fallbacks=[CommandHandler('exit', tg_command.cancel_exit)]
    )
    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', tg_command.delete_start)],
        states={
            tg_command.DELETE_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.delete)]
        },
        fallbacks=[CommandHandler('exit', tg_command.cancel_exit)]
    )
    cls_handler = ConversationHandler(
        entry_points=[CommandHandler('cls', tg_command.cls_start)],
        states={
            tg_command.CLS_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.cls)]
        },
        fallbacks=[CommandHandler('exit', tg_command.cancel_exit)]
    )
    print_handler = ConversationHandler(
        entry_points=[CommandHandler('print', tg_command.print_start)],
        states={
            tg_command.PRINT_KEY: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_command.print_directory)]
        },
        fallbacks=[CommandHandler('exit', tg_command.cancel_exit)]
    )

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(end_handler)
    dispatcher.add_handler(add_handler)
    dispatcher.add_handler(edit_handler)
    dispatcher.add_handler(delete_handler)
    dispatcher.add_handler(cls_handler)
    dispatcher.add_handler(print_handler)

    updater.start_polling()
    updater.idle()

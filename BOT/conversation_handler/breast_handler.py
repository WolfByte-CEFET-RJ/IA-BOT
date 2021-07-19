from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)



def breast_handler(start, SELECT_DISEASE, select_disease, cancel_cmd):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DISEASE: [MessageHandler(Filters.text & ~Filters.command, select_disease)] 
        },
        fallbacks=[CommandHandler('cancel', cancel_cmd)],
    )
    return conv_handler

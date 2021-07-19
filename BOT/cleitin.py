import numpy as np
from rede import breast_cancer_predict,cardio_disease_predict,chronic_kidney_predict

import logging
from ttk import passwd
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
    

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Start of main flow -------------------------------------------------------
SELECT_DISEASE = range(1)

def start(update: Update, _: CallbackContext) -> int:
    disease_reply_keyboard = [['Câncer de mama', 'Doença Cardiovascular', 'Doença hepática']]

    user = update.effective_user

    update.message.reply_text(
        f'Olá {user.first_name}, meu nome é Cleitin do SUS. Esse é um teste de integração com a rede:\n\n'
        'Envie /cancel se quiser parar de falar comigo.',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )

    return SELECT_DISEASE

def select_disease(update: Update, context: CallbackContext) -> int:
    entrada = np.array([[15,8.34,118,988,0.1,0.26,0.88,0.134,0.178,0.2,4,3,23,21,45,43,32,3,2,7,6,5,6,7,6,5,12,32,3,4]])
    resultado = breast_cancer_predict(entrada)
    # Saving disease in context
    text = update.message.text
    context.user_data['disease'] = text

    update.message.reply_text(
        f'Resultado da rede é {resultado}'
    )


def help_cmd(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Use o comando /start para iniciar uma conversa\n\n'
        'Use /cancel para cancelar a conversa'
    )

def cancel_cmd(update: Update, _: CallbackContext) -> int:
    """Ends the conversation when the command /cancel is issued."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Asta la vista, baby.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    updater = Updater(passwd())

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("help", help_cmd))

    # Add conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DISEASE: [MessageHandler(Filters.text & ~Filters.command, select_disease)] 
        },
        fallbacks=[CommandHandler('cancel', cancel_cmd)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()

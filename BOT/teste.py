import numpy as np
from rede import breast_cancer_predict,cardio_disease_predict,chronic_kidney_predict
import sys
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

from conversation_handler.cardio_handler import cardio_handler
from bot_questions.cardio_questions import *
    

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Start of main flow -------------------------------------------------------
SELECT_DISEASE, TEXT_INPUT_ANSWER,TEXT_INPUT_ANSWER1 = range(3)
def start(update: Update, _: CallbackContext) -> int:
    disease_reply_keyboard = [['Câncer de mama', 'Doença Cardiovascular', 'Doença renal crônica']]

    user = update.effective_user

    update.message.reply_text(
        f'Olá {user.first_name}, meu nome é Cleitin do SUS. Esse é um teste de integração com a rede:\n\n'
        'Câncer de mâma \n'
        'Doença cardiovascular \n'
        'Doença renal crônica \n'
        'Envie /cancel se quiser parar de falar comigo.',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )

    return SELECT_DISEASE
  
def text_input(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(
        'Farei várias perguntas para coletar as informações necessárias para a IA,' +
        'peço que responda apenas com os dados pedidos.'
    )
    
    update.message.reply_text(
        'Sua idade (apenas o número):',
    )
    return TEXT_INPUT_ANSWER

def text_input1(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        'Seu genero:',
    )
    return TEXT_INPUT_ANSWER1

def text_input_finish(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        'Vlw flw',
    )
    return ConversationHandler.END


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

    # Add conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DISEASE: [MessageHandler(Filters.text & ~Filters.command, text_input)],
            TEXT_INPUT_ANSWER: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input1
                )
            ],
            TEXT_INPUT_ANSWER1: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input_finish 
                )
            ],
       
        },
        fallbacks=[CommandHandler('cancel', cancel_cmd)],
    ) 

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()

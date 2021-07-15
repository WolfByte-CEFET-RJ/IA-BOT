import logging
from ttk import passwd
from text_input import *

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InputFile
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
# Creating states
SELECT_DISEASE, SELECT_INPUT_TYPE, FILE_INPUT_ANSWER, TEXT_INPUT_ANSWER, TEXT_INPUT_ANSWER1, TEXT_INPUT_ANSWER2, TEXT_INPUT_ANSWER3, TEXT_INPUT_ANSWER4, TEXT_INPUT_ANSWER5, TEXT_INPUT_ANSWER6, TEXT_INPUT_ANSWER7, TEXT_INPUT_ANSWER8, TEXT_INPUT_ANSWER9, TEXT_INPUT_VERIFICATION, TEXT_INPUT_FINISH = range(15)

def start(update: Update, _: CallbackContext) -> int:
    disease_reply_keyboard = [['Main Yasuo', 'Main Yuumi', 'Otaku']]

    user = update.effective_user

    update.message.reply_text(
        f'Olá {user.first_name}, meu nome é Cleitin do SUS. Sou um bot capaz de analisar as seguintes doenças:\n\n'
        'Envie /cancel se quiser parar de falar comigo.',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )

    return SELECT_DISEASE


def select_disease(update: Update, context: CallbackContext) -> int:
    # Saving disease in context
    text = update.message.text
    context.user_data['disease'] = text

    update.message.reply_text(
        f'Você é {text.lower()}?? Ew'
    )

    input_type_reply_keyboard = [['Texto', 'Áudio', 'Arquivo CSV']]
    update.message.reply_text(
        f'Bem, escolha o meio pelo qual prefere fornecer as informações, sr. {text.lower()}',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return SELECT_INPUT_TYPE


def file_input(update: Update, _: CallbackContext) -> int:
    file = open('questions.csv')

    update.message.reply_text('Preencha a tabela com as suas respostas e envie o arquivo de volta')
    update.message.reply_document(InputFile(file, 'Perguntas.csv'))

    return FILE_INPUT_ANSWER


def file_input_answer(update: Update, context: CallbackContext) -> None:
    """
        CSV answer
    """

    # Loading user data
    user_data = context.user_data
    disease = user_data['disease']

    # Recovering user info (demo)
    update.message.reply_text(f'Informações sobre a sua doença: {disease.lower()} recebidas com sucesso')

    msg = update.message.document.get_file()
    msg.download()
    return ConversationHandler.END


# Text input
def text_input(update: Update, context: CallbackContext) -> int:
    """
        Start for capturing user info by text
    """
    update.message.reply_text(
        'Farei várias perguntas para coletar as informações necessárias para a IA,' +
        'peço que responda apenas com os dados pedidos.'
    )

    update.message.reply_text(
        f'Sua idade (apenas o número):',
    )

    return TEXT_INPUT_ANSWER

def text_input_finish(update: Update, context: CallbackContext) -> int:
    """
        FLW
    """

    update.message.reply_text(
        f'Vlw flw',
    )

    return ConversationHandler.END

def audio_input(update: Update, context: CallbackContext) -> int:
    return 1

# End of main flow -------------------------------------------------------


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
    # Create the Updater and pass it your bot's token.
    updater = Updater(passwd())

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("help", help_cmd))

    # Add conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DISEASE: [MessageHandler(Filters.text & ~Filters.command, select_disease)],
            SELECT_INPUT_TYPE: [
                MessageHandler(Filters.regex('^Arquivo CSV$'), file_input),
                MessageHandler(Filters.regex('^Texto$'), text_input),
                MessageHandler(Filters.regex('^Áudio$'), audio_input)
            ],
            FILE_INPUT_ANSWER: [
                MessageHandler(Filters.document & ~Filters.command, file_input_answer)
            ],
            TEXT_INPUT_ANSWER: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input0
                )
            ],
            TEXT_INPUT_ANSWER1: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input1
                )
            ],
            TEXT_INPUT_ANSWER2: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input2
                )
            ],
            TEXT_INPUT_ANSWER3: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input3
                )
            ],
            TEXT_INPUT_ANSWER4: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input4
                )
            ],
            TEXT_INPUT_ANSWER5: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input5
                )
            ],
            TEXT_INPUT_ANSWER6: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input6
                )
            ],
            TEXT_INPUT_ANSWER7: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input7
                )
            ],
            TEXT_INPUT_ANSWER8: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input8
                )
            ],
            TEXT_INPUT_ANSWER9: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input9
                )
            ],
            TEXT_INPUT_VERIFICATION: [
                MessageHandler(
                    Filters.text & ~Filters.command, text_input_verification
                )
            ],
            TEXT_INPUT_FINISH: [
                MessageHandler(
                    Filters.regex('^Não$'), text_input
                ),
                MessageHandler(
                    Filters.text & ~Filters.command, text_input_finish
                )
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel_cmd)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

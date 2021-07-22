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

from verification import input_verification
from conversation_handler.cardio_handler import cardio_handler
from bot_questions.questions import *
    

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Start of main flow -------------------------------------------------------
SELECT_DISEASE, INPUT_ANSWER, INPUT_ANSWER1, INPUT_ANSWER2, \
INPUT_ANSWER3, INPUT_ANSWER4, INPUT_ANSWER5, INPUT_ANSWER6, \
INPUT_ANSWER7, INPUT_ANSWER8, INPUT_ANSWER9, INPUT_ANSWER10, \
INPUT_ANSWER11, INPUT_ANSWER12, INPUT_ANSWER13, INPUT_ANSWER14, \
INPUT_ANSWER15, INPUT_ANSWER16, INPUT_ANSWER17, INPUT_ANSWER18, \
INPUT_ANSWER19, INPUT_ANSWER20, INPUT_ANSWER21, INPUT_ANSWER22, \
INPUT_ANSWER23, INPUT_ANSWER24, INPUT_ANSWER25, INPUT_ANSWER26, \
INPUT_ANSWER27, INPUT_ANSWER28, INPUT_ANSWER29, INPUT_ANSWER30, \
INPUT_VERIFICATION, INPUT_FINISH = range(34) 

def start(update: Update, _: CallbackContext) -> int:
    disease_reply_keyboard = [['Câncer de mama', 'Doença Cardiovascular', 'Doença Renal Crônica']]

    user = update.effective_user

    update.message.reply_text(
        f'Olá, {user.first_name}! Meu nome é Cleitin do SUS. Eu sou capaz de'
        'analisar as seguintes doenças:\n\n'
        'Câncer de mâma \n'
        'Doença cardiovascular \n'
        'Doença renal crônica \n'
        'Envie /cancel se quiser parar de falar comigo.',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )

    return SELECT_DISEASE
  
def info_disease(update: Update, context: CallbackContext) -> int:
    disease_reply_keyboard = [['Entendi']]
    
    text = update.message.text
    context.user_data['disease'] = text
    
    if(context.user_data['disease'] == "Câncer de mama"):
        update.message.reply_text(
        'Para realizar a previsão sobre o câncer de mâma, precisarei de algumas '
        'informações que descrevem as caracteristicas dos núcleos celulares ' +
        'presentes nas imagens de diagnóstico. \n\n' +
        'a) raio (média das distâncias do centro até pontos do perímetro) \n'
        'b) textura (desvio padrão dos valores da escala de cinza) \n'
        'c) perímetro \n'
        'd) área \n'
        'e) suavidade (variação local em comprimentos de raio) \n'
        'f) compactação(perimetro^2 / area - 1.0) \n'
        'g) concavidade(severidade das porções côncavas do contorno) \n'
        'h) pontos côncavos(número de porções côncavas do contorno) \n'
        'i) simetria \n'
        'j) dimensão fractal("aproximação até a costa" - 1) \n',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )
        
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
         update.message.reply_text(
        'Para realizar que eu possa analisar a existência de uma doença '
        'cardiovascular, precisarei das seguinte informações: \n\n'
        'a) Idade \n'
        'b) Gênero \n'
        'c) Altura \n'
        'd) Peso \n'
        'e) Pressão arterial sistólica \n'
        'f) Pressão arterial diastólica \n'
        'g) Colesterol \n'
        'h) Glicose \n'
        'i) Fumante \n'
        'j) Ingestao de alcool \n'
        'l) Atividade física',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
         update.message.reply_text(
        'Para realizar que eu possa analisar a existência de uma doença '
        'renal crônica, precisarei das seguinte informações: \n\n'
        'a) Pressão sanguínea \n'
        'b) Gravidade específica \n'
        'c) Albumina \n'
        'd) Açúcar \n'
        'e) Hemácia \n'
        'f) Ureia sanguínea \n'
        'g) Creatina sérica \n'
        'h) Sódio \n'
        'i) Potássio \n'
        'j) Hemoglobina \n'
        'l) Contagem de glóbulos brancos\n'
        'm) Contagem de glóbulos vermelhos\n'
        'n) Hipertensão',
        reply_markup=ReplyKeyboardMarkup(disease_reply_keyboard, one_time_keyboard=True),
    )
        
    
    return INPUT_ANSWER

def input_finish(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        'Vlw flw',
    )
    resposta = context.user_data['respostas']
    
    cardio_disease_predict(resposta)
    print(cardio_disease_predict(resposta))
    
    return ConversationHandler.END


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
    conv_handler = cardio_handler(start,SELECT_DISEASE,info_disease,INPUT_ANSWER,
                   input0,INPUT_ANSWER1,input1,INPUT_ANSWER2,
                   input2,INPUT_ANSWER3,input3,INPUT_ANSWER4,
                   input4,INPUT_ANSWER5,input5,INPUT_ANSWER6,
                   input6,INPUT_ANSWER7,input7,INPUT_ANSWER8,
                   input8,INPUT_ANSWER9,input9,INPUT_ANSWER10,
                   input10,INPUT_ANSWER11,input11,INPUT_ANSWER12,
                   input12,INPUT_ANSWER13,input13,INPUT_ANSWER14,
                   input14,INPUT_ANSWER15,input15,INPUT_ANSWER16,
                   input16,INPUT_ANSWER17,input17,INPUT_ANSWER18,
                   input18,INPUT_ANSWER19,input19,INPUT_ANSWER20,
                   input20,INPUT_ANSWER21,input21,INPUT_ANSWER22,
                   input22,INPUT_ANSWER23,input23,INPUT_ANSWER24,
                   input24,INPUT_ANSWER25,input25,INPUT_ANSWER26,
                   input26,INPUT_ANSWER27,input27,INPUT_ANSWER28,
                   input28,INPUT_ANSWER29,input29,INPUT_ANSWER30,
                   input30,INPUT_VERIFICATION,input_verification,
                   INPUT_FINISH,input_finish,cancel_cmd)
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext
)
import numpy as np


SELECT_DISEASE, INPUT_ANSWER, INPUT_ANSWER1, INPUT_ANSWER2, \
INPUT_ANSWER3, INPUT_ANSWER4, INPUT_ANSWER5, INPUT_ANSWER6, \
INPUT_ANSWER7, INPUT_ANSWER8, INPUT_ANSWER9, INPUT_ANSWER10, \
INPUT_ANSWER11, INPUT_ANSWER12, INPUT_ANSWER13, INPUT_ANSWER14, \
INPUT_ANSWER15, INPUT_ANSWER16, INPUT_ANSWER17, INPUT_ANSWER18, \
INPUT_ANSWER19, INPUT_ANSWER20, INPUT_ANSWER21, INPUT_ANSWER22, \
INPUT_ANSWER23, INPUT_ANSWER24, INPUT_ANSWER25, INPUT_ANSWER26, \
INPUT_ANSWER27, INPUT_ANSWER28, INPUT_ANSWER29, INPUT_ANSWER30, \
INPUT_VERIFICATION, INPUT_FINISH = range(34)



def input_verification(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    #if(context.user_data['disease'] == "Câncer de mama"):
        
        
    if(context.user_data['disease'] == "Doença Cardiovascular"):
        
        context.user_data['atividadefisica'] = text
        
        respostasArray = np.array([])
    
        respostas = {
            'idade': context.user_data['idade'],
            'genero': context.user_data['genero'],
            'altura': context.user_data['altura'],
            'peso': context.user_data['peso'],
            'pressão': context.user_data['sistolica'],
            'pressão2': context.user_data['diastolica'],
            'colesterol': context.user_data['colesterol'],
            'glicose': context.user_data['glicose'],
            'fumante': context.user_data['fumante'],
            'atividade física': context.user_data['atividadefisica'],
        }
    
    
        for k, v in respostas.items():
            update.message.reply_text(f'{k}: {v}')
            respostasArray.append(v)
            
        context.user_data['respostas'] = respostasArray
        
    
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
            'Confirma essas opções acima?',
            reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
    return INPUT_FINISH


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
INPUT_ANSWER27, INPUT_ANSWER28, INPUT_ANSWER29, \
INPUT_VERIFICATION, INPUT_FINISH = range(33)



def input_verification(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    respostasList = []
    
    if(context.user_data['disease'] == "Câncer de mama"):
        context.user_data['fractal_wst'] = float(text)
        respostasObj = {
            'raio_media': context.user_data['raio_media'],
            'textura_media': context.user_data['textura_media'],
            'perimetro_media': context.user_data['perimetro_media'], 
            'area_media': context.user_data['area_media'],
            'suavidade_media': context.user_data['suavidade_media'],
            'compactacao_media': context.user_data['compactacao_media'],
            'concavidade_media': context.user_data['concavidade_media'],
            'pontos_concavos_media': context.user_data['pontos_concavos_media'],
            'simetria_media': context.user_data['simetria_media'],
            'fractal_media': context.user_data['fractal_media'],
            'raio_EP': context.user_data['raio_EP'],
            'textura_EP': context.user_data['textura_EP'],
            'perimetro_EP': context.user_data['perimetro_EP'], 
            'area_EP': context.user_data['area_EP'],
            'suavidade_EP': context.user_data['suavidade_EP'],
            'compactacao_EP': context.user_data['compactacao_EP'],
            'concavidade_EP': context.user_data['concavidade_EP'],
            'pontos_concavos_EP': context.user_data['pontos_concavos_EP'],
            'simetria_EP': context.user_data['simetria_EP'],
            'fractal_EP': context.user_data['fractal_EP'],
            'raio_wst': context.user_data['raio_wst'],
            'textura_wst': context.user_data['textura_wst'],
            'perimetro_wst': context.user_data['perimetro_wst'], 
            'area_wst': context.user_data['area_wst'],
            'suavidade_wst': context.user_data['suavidade_wst'],
            'compactacao_wst': context.user_data['compactacao_wst'],
            'concavidade_wst': context.user_data['concavidade_wst'],
            'pontos_concavos_wst': context.user_data['pontos_concavos_wst'],
            'simetria_wst': context.user_data['simetria_wst'],
            'fractal_wst': context.user_data['fractal_wst'],
        }
        
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        
        if(text == 'Sim'):
            context.user_data['atividadefisica'] = 1
        else:
             context.user_data['atividadefisica'] = 0
        
        respostasObj = {
            'idade': context.user_data['idade'],
            'altura': context.user_data['altura'],
            'peso': context.user_data['peso'], 
            'genero': context.user_data['genero'],
            'pressão': context.user_data['sistolica'],
            'pressão2': context.user_data['diastolica'],
            'colesterol': context.user_data['colesterol'],
            'glicose': context.user_data['glicose'],
            'fumante': context.user_data['fumante'],
            'alcool': context.user_data['alcool'],
            'atividade física': context.user_data['atividadefisica'],
        }
        
        
    for k, v in respostasObj.items():
        update.message.reply_text(f'{k}: {v}')
        respostasList.append(v)
        
    context.user_data['inputsRede'] = np.array(respostasList)

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Confirma essas opções acima?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )
    return INPUT_FINISH


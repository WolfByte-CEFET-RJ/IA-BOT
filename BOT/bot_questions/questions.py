from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext
)


SELECT_DISEASE, INPUT_ANSWER, INPUT_ANSWER1, INPUT_ANSWER2, \
INPUT_ANSWER3, INPUT_ANSWER4, INPUT_ANSWER5, INPUT_ANSWER6, \
INPUT_ANSWER7, INPUT_ANSWER8, INPUT_ANSWER9, INPUT_ANSWER10, \
INPUT_ANSWER11, INPUT_ANSWER12, INPUT_ANSWER13, INPUT_ANSWER14, \
INPUT_ANSWER15, INPUT_ANSWER16, INPUT_ANSWER17, INPUT_ANSWER18, \
INPUT_ANSWER19, INPUT_ANSWER20, INPUT_ANSWER21, INPUT_ANSWER22, \
INPUT_ANSWER23, INPUT_ANSWER24, INPUT_ANSWER25, INPUT_ANSWER26, \
INPUT_ANSWER27, INPUT_ANSWER28, INPUT_ANSWER29, INPUT_ANSWER30, \
INPUT_VERIFICATION, INPUT_FINISH = range(34)


def input0(update: Update, context: CallbackContext) -> int:
    
    if(context.user_data['disease'] == "Câncer de mama"):
        update.message.reply_text(
        'raio (média): ',
    )
        
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        update.message.reply_text(
        'Sua idade (apenas o número):',
    )
    
    return INPUT_ANSWER1


def input1(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['raio_media'] = text 
       update.message.reply_text(
       'textura  (média): ',
    )
        
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['idade'] = text
        update.message.reply_text(
        'Sua altura, valor em cm (Exemplo: 175 para um metro e setenta e cinco centímetros): ',
    )

    
    return INPUT_ANSWER2

def input2(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura_media'] = text 
       update.message.reply_text(
       'perímetro (média): ',
    )
       
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['altura'] = text
        update.message.reply_text(
        'Seu peso, apenas kilogramas (Exemplo: 78 para setenta e oito kilos):'
    )

    return INPUT_ANSWER3

def input3(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['perimetro_media'] = text 
       update.message.reply_text(
       'área (média): ',
    )
   
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['peso'] = text 
        input_type_reply_keyboard = [['Masculino', 'Feminino']]
        update.message.reply_text(
        'Seu genero :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER4



def input4(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['area_media'] = text 
       update.message.reply_text(
       'suavidade (média): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['genero'] = text 
        update.message.reply_text(
            'Sua pressão arterial sistólica:',
        )

    return INPUT_ANSWER5



def input5(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['suavidade_media'] = text 
       update.message.reply_text(
       'compactação (média): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        text = update.message.text
        context.user_data['sistolica'] = text
        update.message.reply_text(
            'Sua pressão arterial diastólica:',
        )

    return INPUT_ANSWER6



def input6(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['compactacao_media'] = text 
       update.message.reply_text(
       'concavidade (média): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['diastolica'] = text
        input_type_reply_keyboard = [['1', '2', '3']]
        update.message.reply_text(
            'Seu colesterol (1: normal, 2: acima do normal, 3: muito acima do normal) :',
            reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )

    return INPUT_ANSWER7



def input7(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['concavidade_media'] = text 
       update.message.reply_text(
       'pontos_concavos  (média): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['colesterol'] = int(text)
    
        input_type_reply_keyboard = [['1', '2', '3']]
        update.message.reply_text(
            'Seu glicose (1: normal, 2: acima do normal, 3: muito acima do normal) :',
            reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )

    return INPUT_ANSWER8



def input8(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_media'] = text 
       update.message.reply_text(
       'simetria  (média): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['glicose'] = int(text)
    
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
            'Fumante?',
            reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )

    return INPUT_ANSWER9



def input9(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['simetria_media'] = text 
       update.message.reply_text(
       'dimensão fractal (média): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['fumante'] = text
    
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
            'Ingestão de álcool?',
            reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )

    return INPUT_ANSWER10

def input10(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['fractal_media'] = text 
       update.message.reply_text(
       'raio (erro padrão): ',
    )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['alcool'] = text 
    
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
            'Pratica atividades físicas? :',
            reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        return INPUT_FINISH

    return INPUT_ANSWER11

def input11(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['raio_EP'] = text 
       update.message.reply_text(
       'textura  (erro padrão): ',
    )

    return INPUT_ANSWER12

def input12(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura_EP'] = text 
       update.message.reply_text(
       'perímetro   (erro padrão): ',
    )
       
    return INPUT_ANSWER13

def input13(update: Update, context: CallbackContext) -> int:
    text = update.message.text

    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['perimetro_EP'] = text 
       update.message.reply_text(
       'área (erro padrão): ',
    )

    return INPUT_ANSWER14

def input14(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['area_EP'] = text 
       update.message.reply_text(
       'suavidade (erro padrão): ',
    )
    
    return INPUT_ANSWER15

def input15(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['suavidade_EP'] = text 
       update.message.reply_text(
       'compactação (erro padrão): ',
    )

    return INPUT_ANSWER16

def input16(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['compactacao_EP'] = text 
       update.message.reply_text(
       'concavidade (erro padrão): ',
    )

    return INPUT_ANSWER17

def input17(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['concavidade_EP'] = text 
       update.message.reply_text(
       'pontos côncavos (erro padrão): ',
    )

    return INPUT_ANSWER18

def input18(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_EP'] = text 
       update.message.reply_text(
       'simetria (erro padrão): ',
    )

    return INPUT_ANSWER19

def input19(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['simetria_EP'] = text 
       update.message.reply_text(
       'dimensão fractual (erro padrão): ',
    )

    return INPUT_ANSWER20

def input20(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['fractual_EP'] = text 
       update.message.reply_text(
       'raio (worst): ',
    )

    return INPUT_ANSWER21

def input21(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['raio_wst'] = text 
       update.message.reply_text(
       'textura  (worst): ',
    )

    return INPUT_ANSWER22

def input22(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura_wst'] = text 
       update.message.reply_text(
       'perímetro   (worst): ',
    )
 
    return INPUT_ANSWER23

def input23(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['perimetro_wst'] = text 
       update.message.reply_text(
       'área    (worst): ',
    )

    return INPUT_ANSWER24

def input24(update: Update, context: CallbackContext) -> int:
    text = update.message.text
   
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['area_wst'] = text 
       update.message.reply_text(
       'suavidade (worst): ',
    )

    return INPUT_ANSWER25

def input25(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['suavidade_wst'] = text 
       update.message.reply_text(
       'compactação  (worst): ',
    )

    return INPUT_ANSWER26

def input26(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['compactacao_wst'] = text 
       update.message.reply_text(
       'concavidade (worst): ',
    )

    return INPUT_ANSWER27

def input27(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['concavidade_wst'] = text 
       update.message.reply_text(
       'pontos côncavos (worst): ',
    )

    return INPUT_ANSWER28

def input28(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_wst'] = text 
       update.message.reply_text(
       'simetria (worst): ',
    )

    return INPUT_ANSWER29

def input29(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_wst'] = text 
       update.message.reply_text(
       'dimensão fractal  (worst): ',
    )

    return INPUT_ANSWER30

def input30(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_wst'] = text 
       update.message.reply_text(
       'simetria (worst): ',
    )

    #return INPUT_VERIFICATION
    return INPUT_FINISH



def input_verification(update: Update, context: CallbackContext) -> int:

    text = update.message.text
    context.user_data['atividadefisica'] = text

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

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Confirma essas opções acima?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_FINISH
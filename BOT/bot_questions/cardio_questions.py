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
       context.user_data['raio'] = text 
       update.message.reply_text(
       'textura  (média): ',
    )
       
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['idade'] = text 
        input_type_reply_keyboard = [['Masculino', 'Feminino']]
        update.message.reply_text(
        'Seu genero :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    
    return INPUT_ANSWER2

def input2(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura'] = text 
       update.message.reply_text(
       'perímetrio (média): ',
    )
       
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['genero'] = text
        update.message.reply_text(
        'Sua altura, valor em cm (Exemplo: 175 para um metro e setenta e cinco centímetros): ',
    )

    return INPUT_ANSWER2

def input3(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura'] = text 
       update.message.reply_text(
       'perímetrio (média): ',
    )
       
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['genero'] = text
        update.message.reply_text(
        'Sua altura, valor em cm (Exemplo: 175 para um metro e setenta e cinco centímetros): ',
    )
    context.user_data['altura'] = int(text)

    update.message.reply_text(
        'Seu peso, apenas kilogramas (Exemplo: 78 para setenta e oito kilos):',
    )

    return INPUT_ANSWER3



def input4(update: Update, context: CallbackContext) -> int:
    """
        Pergunta Pressão sistólica
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['peso'] = text

    update.message.reply_text(
        'Sua pressão arterial sistólica:',
    )

    return INPUT_ANSWER4



def input5(update: Update, context: CallbackContext) -> int:
    """
        Pergunta pressão diastólica
    """
    text = update.message.text
    context.user_data['sistolica'] = text

    update.message.reply_text(
        'Sua pressão arterial diastólica:',
    )

    return INPUT_ANSWER5



def input6(update: Update, context: CallbackContext) -> int:
    """
        Pergunta Colesterol
    """
    text = update.message.text
    context.user_data['diastolica'] = text

    input_type_reply_keyboard = [['1', '2', '3']]
    update.message.reply_text(
        'Seu colesterol (1: normal, 2: acima do normal, 3: muito acima do normal) :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER6



def input7(update: Update, context: CallbackContext) -> int:
    """
        Pergunta Glicose
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['colesterol'] = int(text)

    input_type_reply_keyboard = [['1', '2', '3']]
    update.message.reply_text(
        'Seu glicose (1: normal, 2: acima do normal, 3: muito acima do normal) :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER7



def input8(update: Update, context: CallbackContext) -> int:
    """
        Pergunta Fumante
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['glicose'] = int(text)

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Fumante?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER8



def input9(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER9

def input10(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER10

def input11(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER11

def input12(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER12

def input13(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER13

def input14(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER14

def input15(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER15

def input16(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER16

def input17(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER17

def input18(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER18

def input19(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER19

def input20(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER20

def input21(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER21

def input22(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER22

def input23(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER23

def input24(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER24

def input25(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER25

def input26(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER26

def input27(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER27

def input28(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER28

def input29(update: Update, context: CallbackContext) -> int:
    """
        Pergunta alcool
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['fumante'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return INPUT_ANSWER29

def input30(update: Update, context: CallbackContext) -> int:
    """
        Pergunta atividade física
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['alcool'] = text

    input_type_reply_keyboard = [['Sim', 'Não']]
    update.message.reply_text(
        'Pratica atividades físicas? :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
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
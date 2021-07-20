from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext
)
SELECT_DISEASE, TEXT_INPUT_ANSWER, TEXT_INPUT_ANSWER1, TEXT_INPUT_ANSWER2, TEXT_INPUT_ANSWER3, TEXT_INPUT_ANSWER4, TEXT_INPUT_ANSWER5, TEXT_INPUT_ANSWER6, TEXT_INPUT_ANSWER7, TEXT_INPUT_ANSWER8, TEXT_INPUT_ANSWER9, TEXT_INPUT_VERIFICATION, TEXT_INPUT_FINISH = range(13)



def text_input0(update: Update, context: CallbackContext) -> int:
    """
        Pergunta genero
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['idade'] = text

    input_type_reply_keyboard = [['Masculino', 'Feminino']]
    update.message.reply_text(
        'Seu genero :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
    )

    return TEXT_INPUT_ANSWER1



def text_input1(update: Update, context: CallbackContext) -> int:
    """
        Pergunta Altura
    """
    text = update.message.text
    context.user_data['genero'] = text

    update.message.reply_text(
        'Sua altura, valor em cm (Exemplo: 175 para um metro e setenta e cinco centímetros): ',
    )

    return TEXT_INPUT_ANSWER2



def text_input2(update: Update, context: CallbackContext) -> int:
    """
        Pergunta peso
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['altura'] = int(text)

    update.message.reply_text(
        'Seu peso, apenas kilogramas (Exemplo: 78 para setenta e oito kilos):',
    )

    return TEXT_INPUT_ANSWER3



def text_input3(update: Update, context: CallbackContext) -> int:
    """
        Pergunta Pressão sistólica
    """
    # Saving disease in context
    text = update.message.text
    context.user_data['peso'] = text

    update.message.reply_text(
        'Sua pressão arterial sistólica:',
    )

    return TEXT_INPUT_ANSWER4



def text_input4(update: Update, context: CallbackContext) -> int:
    """
        Pergunta pressão diastólica
    """
    text = update.message.text
    context.user_data['sistolica'] = text

    update.message.reply_text(
        'Sua pressão arterial diastólica:',
    )

    return TEXT_INPUT_ANSWER5



def text_input5(update: Update, context: CallbackContext) -> int:
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

    return TEXT_INPUT_ANSWER6



def text_input6(update: Update, context: CallbackContext) -> int:
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

    return TEXT_INPUT_ANSWER7



def text_input7(update: Update, context: CallbackContext) -> int:
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

    return TEXT_INPUT_ANSWER8



def text_input8(update: Update, context: CallbackContext) -> int:
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

    return TEXT_INPUT_ANSWER9



def text_input9(update: Update, context: CallbackContext) -> int:
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

    return TEXT_INPUT_VERIFICATION
    # return ConversationHandler.END



def text_input_verification(update: Update, context: CallbackContext) -> int:

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

    return TEXT_INPUT_FINISH
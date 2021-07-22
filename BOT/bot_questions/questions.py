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
        'Raio (média): ',
        )
        
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        update.message.reply_text(
        'Sua idade (apenas o número): ',
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        update.message.reply_text(
        'Sua pressão sanguínea (Apenas o valor numérico): '        
        )
    
    return INPUT_ANSWER1


def input1(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['raio_media'] = text 
       update.message.reply_text(
       'Textura  (média): ',
       )
        
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['idade'] = text
        update.message.reply_text(
        'Sua altura, valor em cm (Exemplo: 175 para um metro e setenta e cinco centímetros): ',
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Bp'] = text
        update.message.reply_text(
        'Sua gravidade específica (Apenas o valor numérico): '        
        )
    
    return INPUT_ANSWER2

def input2(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura_media'] = text 
       update.message.reply_text(
       'Perímetro (média): ',
       )
       
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['altura'] = text
        update.message.reply_text(
        'Seu peso, apenas kilogramas (Exemplo: 78 para setenta e oito kilos):'
        )

    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Sg'] = text
        update.message.reply_text(
        'Sua albumina (Apenas o valor numérico):  '        
        )
        
    return INPUT_ANSWER3

def input3(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['perimetro_media'] = text 
       update.message.reply_text(
       'Área (média): ',
       )
   
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['peso'] = text 
        input_type_reply_keyboard = [['Masculino', 'Feminino']]
        update.message.reply_text(
        'Seu genero :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Al'] = text
        update.message.reply_text(
        'Seu açúcar (Apenas o valor numérico): '        
        )

    return INPUT_ANSWER4



def input4(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['area_media'] = text 
       update.message.reply_text(
       'Suavidade (média): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['genero'] = text 
        update.message.reply_text(
        'Sua pressão arterial sistólica:',
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Su'] = text
        input_type_reply_keyboard = [['0.0', '1.0']]
        update.message.reply_text(
        'Suas hemácias: '  ,
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )


    return INPUT_ANSWER5



def input5(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['suavidade_media'] = text 
       update.message.reply_text(
       'Compactação (média): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        text = update.message.text
        context.user_data['sistolica'] = text
        update.message.reply_text(
        'Sua pressão arterial diastólica:',
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Rbc'] = text
        update.message.reply_text(
        'Sua uréia sanguínea (Apenas o valor numérico): '        
        )

        
    return INPUT_ANSWER6



def input6(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['compactacao_media'] = text 
       update.message.reply_text(
       'Concavidade (média): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['diastolica'] = text
        input_type_reply_keyboard = [['1', '2', '3']]
        update.message.reply_text(
        'Seu colesterol (1: normal, 2: acima do normal, 3: muito acima do normal) :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Bu'] = text
        update.message.reply_text(
        'Sua creatina sérica (Apenas o valor numérico): '        
        )


    return INPUT_ANSWER7



def input7(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['concavidade_media'] = text 
       update.message.reply_text(
       'Pontos Concavos  (média): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['colesterol'] = int(text)
    
        input_type_reply_keyboard = [['1', '2', '3']]
        update.message.reply_text(
        'Seu glicose (1: normal, 2: acima do normal, 3: muito acima do normal) :',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Sc'] = text
        update.message.reply_text(
        'Seu sódio (Apenas o valor numérico): '        
        )


    return INPUT_ANSWER8



def input8(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_media'] = text 
       update.message.reply_text(
       'Simetria  (média): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['glicose'] = int(text)
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
        'Fumante?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
    
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Sod'] = text
        update.message.reply_text(
        'Seu potássio (Apenas o valor numérico): '        
        )


    return INPUT_ANSWER9



def input9(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['simetria_media'] = text 
       update.message.reply_text(
       'Dimensão fractal (média): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['fumante'] = text
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
        'Ingestão de álcool?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Pot'] = text
        update.message.reply_text(
        'Sua hemoglobina (Apenas o valor numérico): '        
        )


    return INPUT_ANSWER10

def input10(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['fractal_media'] = text 
       update.message.reply_text(
       'Raio (erro padrão): ',
       )
    
    elif(context.user_data['disease'] == "Doença Cardiovascular"):
        context.user_data['alcool'] = text 
    
        input_type_reply_keyboard = [['Sim', 'Não']]
        update.message.reply_text(
        'Pratica atividades físicas?',
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        return INPUT_VERIFICATION
    
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Hemo'] = text
        update.message.reply_text(
        'Contagem dos glóbulos brancos (Apenas o valor numérico): '        
        )

    return INPUT_ANSWER11

def input11(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['raio_EP'] = text 
       update.message.reply_text(
       'Textura  (erro padrão): ',
       )
       
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Wbcc'] = text
        update.message.reply_text(
        'Contagem dos glóbulos vermelhos (Apenas o valor numérico): '        
        )


    return INPUT_ANSWER12

def input12(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura_EP'] = text 
       update.message.reply_text(
       'Perímetro   (erro padrão): ',
       )
       
    elif(context.user_data['disease'] == "Doença Renal Crônica"):
        context.user_data['Rbcc'] = text
        input_type_reply_keyboard = [['Sim', 'Não']],
        update.message.reply_text(
        'Você tem hipertensão? ', 
        reply_markup=ReplyKeyboardMarkup(input_type_reply_keyboard, one_time_keyboard=True),
        )
        return INPUT_FINISH

       
    return INPUT_ANSWER13

def input13(update: Update, context: CallbackContext) -> int:
    text = update.message.text

    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['perimetro_EP'] = text 
       update.message.reply_text(
       'Área (erro padrão): ',
    )
       

    return INPUT_ANSWER14

def input14(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['area_EP'] = text 
       update.message.reply_text(
       'Suavidade (erro padrão): ',
    )
    
    return INPUT_ANSWER15

def input15(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['suavidade_EP'] = text 
       update.message.reply_text(
       'Compactação (erro padrão): ',
    )

    return INPUT_ANSWER16

def input16(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['compactacao_EP'] = text 
       update.message.reply_text(
       'Concavidade (erro padrão): ',
    )

    return INPUT_ANSWER17

def input17(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['concavidade_EP'] = text 
       update.message.reply_text(
       'Pontos côncavos (erro padrão): ',
    )

    return INPUT_ANSWER18

def input18(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_EP'] = text 
       update.message.reply_text(
       'Simetria (erro padrão): ',
    )

    return INPUT_ANSWER19

def input19(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['simetria_EP'] = text 
       update.message.reply_text(
       'Dimensão fractual (erro padrão): ',
    )

    return INPUT_ANSWER20

def input20(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['fractual_EP'] = text 
       update.message.reply_text(
       'Raio (worst): ',
    )

    return INPUT_ANSWER21

def input21(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['raio_wst'] = text 
       update.message.reply_text(
       'Textura  (worst): ',
    )

    return INPUT_ANSWER22

def input22(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['textura_wst'] = text 
       update.message.reply_text(
       'Perímetro   (worst): ',
    )
 
    return INPUT_ANSWER23

def input23(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['perimetro_wst'] = text 
       update.message.reply_text(
       'Àrea    (worst): ',
    )

    return INPUT_ANSWER24

def input24(update: Update, context: CallbackContext) -> int:
    text = update.message.text
   
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['area_wst'] = text 
       update.message.reply_text(
       'Suavidade (worst): ',
    )

    return INPUT_ANSWER25

def input25(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['suavidade_wst'] = text 
       update.message.reply_text(
       'Compactação  (worst): ',
    )

    return INPUT_ANSWER26

def input26(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['compactacao_wst'] = text 
       update.message.reply_text(
       'Concavidade (worst): ',
    )

    return INPUT_ANSWER27

def input27(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['concavidade_wst'] = text 
       update.message.reply_text(
       'Pontos côncavos (worst): ',
    )

    return INPUT_ANSWER28

def input28(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_wst'] = text 
       update.message.reply_text(
       'Simetria (worst): ',
    )

    return INPUT_ANSWER29

def input29(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_wst'] = text 
       update.message.reply_text(
       'Dimensão fractal  (worst): ',
    )

    return INPUT_ANSWER30

def input30(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    
    if(context.user_data['disease'] == "Câncer de mama"):
       context.user_data['pontos_concavos_wst'] = text 
       update.message.reply_text(
       'Simetria (worst): ',
    )

    #return INPUT_VERIFICATION
    return INPUT_FINISH



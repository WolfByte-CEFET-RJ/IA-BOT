from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

 
def cardio_handler(start,SELECT_DISEASE,text_input,TEXT_INPUT_ANSWER,
                   text_input0,TEXT_INPUT_ANSWER1,text_input1,TEXT_INPUT_ANSWER2,
                   text_input2,TEXT_INPUT_ANSWER3,text_input3,TEXT_INPUT_ANSWER4,
                   text_input4,TEXT_INPUT_ANSWER5,text_input5,TEXT_INPUT_ANSWER6,
                   text_input6,TEXT_INPUT_ANSWER7,text_input7,TEXT_INPUT_ANSWER8,
                   text_input8,TEXT_INPUT_ANSWER9,text_input9,
                   TEXT_INPUT_VERIFICATION,text_input_verification,TEXT_INPUT_FINISH,
                   text_input_finish,cancel_cmd):
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DISEASE: [MessageHandler(Filters.text & ~Filters.command, text_input)],
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
    return conv_handler
    


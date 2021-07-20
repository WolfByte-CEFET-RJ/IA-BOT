from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

 
def cardio_handler(start,SELECT_DISEASE,info_disease,INPUT_ANSWER,
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
                   INPUT_FINISH,input_finish,cancel_cmd):
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DISEASE: [MessageHandler(Filters.text & ~Filters.command, info_disease)],
            INPUT_ANSWER: [
                MessageHandler(
                    Filters.text & ~Filters.command, input0
                )
            ],
            INPUT_ANSWER1: [
                MessageHandler(
                    Filters.text & ~Filters.command, input1
                )
            ],
            INPUT_ANSWER2: [
                MessageHandler(
                    Filters.text & ~Filters.command, input2
                )
            ],
            INPUT_ANSWER3: [
                MessageHandler(
                    Filters.text & ~Filters.command, input3
                )
            ],
            INPUT_ANSWER4: [
                MessageHandler(
                    Filters.text & ~Filters.command, input4
                )
            ],
            INPUT_ANSWER5: [
                MessageHandler(
                    Filters.text & ~Filters.command, input5
                )
            ],
            INPUT_ANSWER6: [
                MessageHandler(
                    Filters.text & ~Filters.command, input6
                )
            ],
            INPUT_ANSWER7: [
                MessageHandler(
                    Filters.text & ~Filters.command, input7
                )
            ],
            INPUT_ANSWER8: [
                MessageHandler(
                    Filters.text & ~Filters.command, input8
                )
            ],
            INPUT_ANSWER9: [
                MessageHandler(
                    Filters.text & ~Filters.command, input9
                )
            ],
            INPUT_ANSWER10: [
                MessageHandler(
                    Filters.text & ~Filters.command, input10
                )
            ],
            INPUT_ANSWER11: [
                MessageHandler(
                    Filters.text & ~Filters.command, input11
                )
            ],
            INPUT_ANSWER12: [
                MessageHandler(
                    Filters.text & ~Filters.command, input12
                )
            ],
            INPUT_ANSWER13: [
                MessageHandler(
                    Filters.text & ~Filters.command, input13
                )
            ],
            INPUT_ANSWER14: [
                MessageHandler(
                    Filters.text & ~Filters.command, input14
                )
            ],
            INPUT_ANSWER15: [
                MessageHandler(
                    Filters.text & ~Filters.command, input15
                )
            ],
            INPUT_ANSWER16: [
                MessageHandler(
                    Filters.text & ~Filters.command, input16
                )
            ],
            INPUT_ANSWER17: [
                MessageHandler(
                    Filters.text & ~Filters.command, input17
                )
            ],
            INPUT_ANSWER18: [
                MessageHandler(
                    Filters.text & ~Filters.command, input18
                )
            ],
            INPUT_ANSWER19: [
                MessageHandler(
                    Filters.text & ~Filters.command, input19
                )
            ],
            INPUT_ANSWER20: [
                MessageHandler(
                    Filters.text & ~Filters.command, input20
                )
            ],
            INPUT_ANSWER21: [
                MessageHandler(
                    Filters.text & ~Filters.command, input21
                )
            ],
            INPUT_ANSWER22: [
                MessageHandler(
                    Filters.text & ~Filters.command, input22
                )
            ],
            INPUT_ANSWER23: [
                MessageHandler(
                    Filters.text & ~Filters.command, input23
                )
            ],
            INPUT_ANSWER24: [
                MessageHandler(
                    Filters.text & ~Filters.command, input24
                )
            ],
            INPUT_ANSWER25: [
                MessageHandler(
                    Filters.text & ~Filters.command, input25
                )
            ],
            INPUT_ANSWER26: [
                MessageHandler(
                    Filters.text & ~Filters.command, input26
                )
            ],
            INPUT_ANSWER27: [
                MessageHandler(
                    Filters.text & ~Filters.command, input27
                )
            ],
            INPUT_ANSWER28: [
                MessageHandler(
                    Filters.text & ~Filters.command, input28
                )
            ],
            INPUT_ANSWER29: [
                MessageHandler(
                    Filters.text & ~Filters.command, input29
                )
            ],
            
            INPUT_ANSWER30: [
                MessageHandler(
                    Filters.text & ~Filters.command, input30
                )
            ],

            INPUT_VERIFICATION: [
                MessageHandler(
                    Filters.text & ~Filters.command, input_verification
                )
            ],
            INPUT_FINISH: [
                MessageHandler(
                    Filters.text & ~Filters.command, input_finish
                )
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel_cmd)],
    ) 
    return conv_handler
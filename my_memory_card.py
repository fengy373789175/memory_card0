#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import *


app = QApplication([])
main_win = QWidget()
main_line = QVBoxLayout()
Question_line = QHBoxLayout()
midl_line = QHBoxLayout()
bot_line = QHBoxLayout()
question = QLabel('р')

layout_line3 = QVBoxLayout()

result_table = QLabel('anslkjdn')


main_win.total = 0
main_win.score = 0



ansverbot = QPushButton('ответ')
Question_line.addWidget(question)

RadioGroupBox = QGroupBox('Варианты ответов')
answerGroupBox = QGroupBox('Результат')
answerlabel = QLabel('Результат')
answerGroupBox.hide()
answerlayout = QVBoxLayout()
answerlayout.addWidget(answerlabel)
answerGroupBox.setLayout(answerlayout)

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('алеуты')

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answer)


midl_line.addWidget(RadioGroupBox)
midl_line.addWidget(answerGroupBox)

bot_line.addWidget(ansverbot)

main_line.addLayout(Question_line)
main_line.addLayout(midl_line)
main_line.addLayout(bot_line)




layout_line3.addWidget(ansverbot, stretch=2)


layout_card = QVBoxLayout()
layout = QVBoxLayout()
layout_card.setSpacing(5)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def check_answer():
    if answer[0].isChecked():
        show_result(True)
    else:
        show_result(False)

def click_on():
    if ansverbot.text() == 'ответить':
        check_answer()
    else:
        next_question()

def ask(q):
    answerGroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    question.setText(q.question)
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    Question.setText(q.question)
    ansverbot.setText('Ответить')


def show_result():
    if res:
        RadioGroupBox.hide()
        answerGroupBox.show()
        result_table.setText('Правильно')
        main_win.score +=1

    else:
        RadioGroupBox.hide()
        answerGroupBox.show()
        result_table.setText('Невернно')
    ansverbot.setText('Следующий вопрос')





def next_question():
    main_win.total += 1
    sco = int(main_win.score/main_win.total*100)
    print('Твоя статистика', sco, '%', '\n Кол-во верных ответов' , main_win.score, '\n Кол-во всех ответов:', main_win.total)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)







class Question():
    def __init__(
    self, question, right_answer,
    wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



question_list = [Question('Государственный язык португалии','Португалский','Английский', 'Испанский', 'Французкий')]

ansverbot.clicked.connect(click_on)
main_win.setLayout(main_line)
main_win.show()
app.exec_()

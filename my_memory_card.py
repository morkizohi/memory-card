from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QLabel,QMessageBox,QRadioButton,QVBoxLayout,QGroupBox
from random import shuffle
 
class Qustion():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    Answer.show()
    RadioGroup.hide()
    button_asw.setText('Следующий вопрос')


def connector():
    if button_asw.text() == 'Следующий вопрос':
        select_qustion()
    else:
        show_result()
    

def select_qustion():
    Answer.hide()
    RadioGroup.show()
    button_asw.setText('Ответить')
    main_win.current_qustion = main_win.current_qustion + 1 
    if main_win.current_qustion >= len(question_list):
        main_win.current_qustion = 0
    q = question_list[main_win.current_qustion]
    ask(q)





def ask(q:Qustion):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    labl1.setText(q.question)
    Rite.setText(q.right_answer)



app = QApplication([])
main_win = QWidget()
main_win.current_qustion = 0
main_win.setWindowTitle('Memory Card')
main_win.resize(600, 400)

RadioGroup = QGroupBox('Варианты ответов')
Answer = QGroupBox('Результат теста')

question_list =[]
question_list.append(Qustion('Государственный язык Бразилии','Португальский','Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Qustion('Какого цвета нету в триколоре России','Белый','Красный', 'Синий', 'Зеленый'))
question_list.append(Qustion('Какая  валюта у России?','Рубль','Гривна', 'Доллар', 'Марка'))
question_list.append(Qustion('Кто победил в 2 мировой войне?','СССР','Германия', 'Франция', 'США'))
rb1 =QRadioButton('Энцы')
rb2 =QRadioButton('Челымцы')
rb3 =QRadioButton('Смурфы')
rb4 =QRadioButton('Алеуты')

labl1 = QLabel("Какой национальности не существует?")

tmx=QVBoxLayout()
vdm=QHBoxLayout()
amr=QHBoxLayout()
vdm.addWidget(rb1)
vdm.addWidget(rb2)
amr.addWidget(rb3)
amr.addWidget(rb4)
tmx.addLayout(vdm)
tmx.addLayout(amr)

RadioGroup.setLayout(tmx)


main_v_line = QVBoxLayout()




Answer.show()
Right_line = QVBoxLayout()
Right = QLabel("Правильно будет")
Rite = QLabel("Правильный вариант ответа")
Right_line.addWidget(Right)
Answer.setLayout(Right_line)
button_asw = QPushButton("Ответ")
Right_line.addWidget(Rite)



main_v_line.addWidget(labl1, alignment = Qt.AlignCenter)
main_v_line.addWidget(RadioGroup)
main_v_line.addWidget(Answer)

Answer.hide()
main_v_line.addWidget(button_asw, alignment = Qt.AlignCenter)


main_win.setLayout(main_v_line)

answers = [rb1, rb2, rb3, rb4]


button_asw.clicked.connect(connector)

main_win.resize(400, 300)
main_win.show()
app.exec_()
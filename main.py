from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox

Form, Window = uic.loadUiType("KoRadToDo2.0.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

input = open('config.txt', 'r', encoding='utf-8').read().split('\n')
for i in range(1, len(input)):
    form.listWidget.addItem(input[i])
    i += 1

def on_click_calendar():
    form.dateEdit.setDate(form.calendarWidget.selectedDate())

def on_dateEdit_change():
    form.calendarWidget.setSelectedDate(form.dateEdit.date())

def add_edit():
    global finish_date
    finish_date = form.dateEdit.date()
    # берем элемент
    # переменная с текстом из зоны вводa
    item = form.lineEdit.text()
    with open('config.txt', 'a+', encoding='utf-8') as file:
        file.write('\n' + finish_date.toString('dd.MM.yyyy-') + item)
        form.listWidget.addItem(finish_date.toString('dd.MM.yyyy-') + item)
    file.close()

    # после добавления элемента в список, очищается графа ввода
    form.lineEdit.setText("")


def delete_it():
    #захват выбранной строки
    clicked = form.listWidget.currentRow()
    #удаление выбранной строки
    form.listWidget.takeItem(clicked)


def clear_it():
    form.listWidget.clear()
    file = open('config.txt', 'w', encoding='utf-8')
    file.close()

def save_it():
    with open('config.txt', 'w', encoding='utf-8') as fout:
        for i in range(form.listWidget.count()):
            form.listWidget.setCurrentRow(i)
            fout.write('\n' + str(form.listWidget.item(i).text()))

    msg = QMessageBox()
    msg.setWindowTitle("Saved to Database")
    msg.setText("Данные успешно сохранены!")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
    fout.close()


def poisk_data():
    file = open('config.txt', 'r', encoding='utf-8')
    file1 = file.read().split('\n')
    for i in range(1, len(file1)):
        text_split = file1[i].split('-')
        for j in range(0, len(text_split)):
            poisk = form.lineEdit.text()
            if j%2 == 0 and poisk == text_split[j]:
                vivod = text_split[j] + " - " + text_split[j + 1]
                form.listWidget_2.addItem(vivod)
        j += 1
    i += 1
    file.close()
    form.lineEdit.setText("")

def poisk_zadacha():
    file = open('config.txt', 'r', encoding='utf-8')
    file1 = file.read().split('\n')
    for i in range(1, len(file1)):
        text_split = file1[i].split('-')
        for j in range(0, len(text_split)):
            poisk = form.lineEdit.text()
            if j%2 == 1 and poisk == text_split[j]:
                vivod = text_split[j-1] + " - " + text_split[j-2]
                form.listWidget_2.addItem(vivod)
        j += 1
    i += 1
    file.close()
    form.lineEdit.setText("")

def up():
    currentRow = form.listWidget.currentRow()
    currentItem = form.listWidget.takeItem(currentRow)
    form.listWidget.insertItem(currentRow - 1, currentItem)

def down():
    currentRow = form.listWidget.currentRow()
    currentItem = form.listWidget.takeItem(currentRow)
    form.listWidget.insertItem(currentRow + 1, currentItem)

form.pushButton.clicked.connect(add_edit)
form.pushButton_2.clicked.connect(delete_it)
form.pushButton_3.clicked.connect(clear_it)
form.pushButton_6.clicked.connect(save_it)
form.pushButton_5.clicked.connect(poisk_data)
form.pushButton_7.clicked.connect(poisk_zadacha)
form.pushButton_8.clicked.connect(up)
form.pushButton_9.clicked.connect(down)

form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateEdit_change)
start_date = form.calendarWidget.selectedDate()     # переменная с сегоднешним числом
finish_date = form.calendarWidget.selectedDate()    # переменная с числом при нажатии
form.label_3.setText(" Сегодня %s" %start_date.toString('dd-MM-yyyy'))
on_click_calendar()

app.exec_()

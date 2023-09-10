import os
import sys
import pandas as pd

import openai
import json

import subprocess
import requests

from PyQt5.QtGui import QIcon
from qtpy import QtWidgets
from PyQt5.QtWidgets import *
# from PIL import Image
# import matplotlib.pyplot as plt

from QtCreatorChatGPT.codechatgpt import Ui_CodeChatGPT
from QtCreatorChatGPT.firstrowchatgpt import Ui_FirstRowChatGPT
from QtCreatorChatGPT.mainwindow import Ui_MainWindow
from QtCreatorChatGPT.direktchatgpt import Ui_DirektChatGPT
from QtCreatorChatGPT.projektteam import Ui_Projektteam
from QtCreatorChatGPT.tablechatgpt import Ui_TableChatGPT

# API: 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

pfad = None

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION")
        self.ui.actiondirekt.triggered.connect(self.zeigeDirektChatGPTFenster)
        self.ui.actionCode.triggered.connect(self.zeigeCodeChatGPTFenster)
        self.ui.action1_Reihe.triggered.connect(self.zeigeFirstRowChatGPTFenster)
        self.ui.actionTabelle.triggered.connect(self.zeigeTableChatGPTFenster)

        if self.ui.checkAPIKey.isChecked():
            openai.api_key = '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'  #'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'
            print(openai.api_key)
        else:
            print(openai.api_key)
        self.ui.checkAPIKey.clicked.connect(self.getApiKey)

        self.ui.actionLaden.triggered.connect(self.file_laden_dialog)
        self.ui.actionDatei_l_schen.triggered.connect(self.file_delete_dialog)

        self.ui.actionProjektteam.triggered.connect(self.zeigeProjektTeamFenster)

    def getApiKey(self):
        if self.ui.checkAPIKey.isChecked():
            openai.api_key = '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'
            print(openai.api_key)
        else:
            openai.api_key = ""
            print(openai.api_key)

    def file_laden_dialog(self):
        self.ui.file_dialog = QFileDialog()
        self.ui.file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_path, _ = self.ui.file_dialog.getOpenFileName(self, "Datei auswählen")
        self.pfad = str(file_path)

        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        print(file_path)
        self.ui.dateiLabel.setText(f"Ausgewählte Datei: " + file_path)


    def file_delete_dialog(self):
        self.ui.dateiLabel.setText("Keine Datei ausgewählt")



    def zeigeFenster(self, fenster_klasse):
        self.fenster = fenster_klasse()
        self.fenster.show()
        self.close()

    def zeigeDirektChatGPTFenster(self):
        self.zeigeFenster(direktChatGPTFenster)


    def zeigeCodeChatGPTFenster(self):
        self.zeigeFenster(CodeChatGPTFenster)


    def zeigeFirstRowChatGPTFenster(self):
        self.zeigeFenster(FirstRowChatGPTFenster)


    def zeigeTableChatGPTFenster(self):
        self.zeigeFenster(TableChatGPTFenster)


    def zeigeProjektTeamFenster(self):
        self.zeigeFenster(ProjektteamFenster)



class direktChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DirektChatGPT()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - direkt ChatGPT")
        self.dateiLabel = main_window.ui.dateiLabel


        self.ui.pushButton.clicked.connect(self.process_input)

    def button_clicked(self):
        print("button wurde geklickt:", self.dateiLabel.text())

    def process_input(self):
        # Setze deine OpenAI API-Zugriffsschlüssel
        # openai.api_key = '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'

        input_text = self.ui.direktChatInput.toPlainText()

        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=input_text,
                max_tokens=250,  # Anzahl der Tokens in der Antwort
                temperature=0.7,  # Steuerung der Antwortvarianz
                n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
                stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            )
            output=response['choices'][0]['text'].strip()
            token = len(input_text) + len(output)
            # self.ui.direktChatOutput.setPlainText(response['choices'][0]['text'].strip())
            self.ui.direktChatOutput.setPlainText(output)


            self.ui.direktChatGPTToken.setText(str(token))

        except:
            self.ui.direktChatOutput.setStyleSheet("color: red")
            self.ui.direktChatOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!")
            print("Anfrage konnte nicht gesendet werden!")


    def closeEvent(self, event):
        main_window.show()



class CodeChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CodeChatGPT()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - Code ChatGPT")

        self.ui.pushButton.clicked.connect(self.process_input)

        self.ui.btnCodeChatGPTAusfuehren.clicked.connect(self.ausfuehren_input)


    def test_button(name):
        print("MainWindow:", main_window.pfad)


    def ausfuehren_input(self):
        input_text = ""

        print("vor exe")

        self.ui.output("Test")
        exec(self.ui.output)
        print("nach exec")
        # self.ui.CodeChatGPTOutput.setText("{result}")

        # print("test", code_to_execute)
        # print(self.ui.output)
        # ausgabe = exec(code_to_execute)
        # print(exec(self.ui.output))

        # print(ausgabe)


    # script.py für die Ausführung verwenden
    def ausfuehren_script(self):
        # completed_process = subprocess.run(['python', 'script.py'], capture_output=True, test=True)
        # output = completed_process.stdout
        exec(self.ui.output)
        print("{result}")

        # print(output)


    def process_input(self):
        # Setze deine OpenAI API-Zugriffsschlüssel
        # openai.api_key = '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'


        print("1")
        input_text = "schreib python Code um aus einer Tabelle folgende Frage zu lesen."+self.ui.CodeChatGPTInput.toPlainText() + " aus der Tabelle mit dem Pfad: "+main_window.pfad
        print("2")
        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=input_text,
                max_tokens=500,  # Anzahl der Tokens in der Antwort
                temperature=0.7,  # Steuerung der Antwortvarianz
                n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
                stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            )
            print("3")
            # output = exec(response['choices'][0]['text'].strip())
            # self.ui.CodeChatGPTOutput.setPlainText(output)oices' in response:
            #             #     return response['choices'][0]['text'].strip()
            #             # else:
            #             #     return None
            # if response and 'ch
            output = response['choices'][0]['text'].strip()
            token = len(input_text) + len(output)
            print("4/2", output)
            # output = exec(output)
            print("4/3", output)
            self.ui.CodeChatGPTOutput.setPlainText(output)
            self.ui.CoderChatGPTToken.setText(str(token))
            # self.ui.CodeChatGPTOutput.setPlainText(response['choices'][0]['text'].strip())
            # self.ui.CodeChatGPTOutput.setPlainText(response['choices'][0]['text'].strip())
            print("4", print(output))
            self.ui.output = output

            with open('script.py', 'w') as file:
                file.write(output)

        except:
            self.ui.CodeChatGPTOutput.setStyleSheet("color: red")
            self.ui.CodeChatGPTOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!")
            print("Anfrage konnte nicht gesendet werden!")

        print("5")

        return output



    def closeEvent(self, event):
        main_window.show()



class TableChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableChatGPT()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - Table ChatGPT")

        self.ui.btnTable.clicked.connect(self.process_input)

        # csv_filepath = main_window.pfad  # Replace with your CSV file path


    def process_input(self):

        # df = pd.read_csv(csv_filepath)
        # json_data = df.to_json(orient="records")
        #
        #
        #
        #
        # csv = pd.read_csv(main_window.pfad)
        # jsonfile = json.dumps(csv)
        csv = pd.read_csv(main_window.pfad)
        json = csv.to_json(orient="records")

        print("1", json)
        input_text = "beantworte die Frage" + self.ui.tableChatGPTInput.toPlainText()+ "und verwende dazu den folgenden Datensatz:" + json

        print("2")
        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=str(input_text),
                max_tokens=500,  # Anzahl der Tokens in der Antwort
                temperature=0.7,  # Steuerung der Antwortvarianz
                n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
                stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            )
            print("3")
            # output = exec(response['choices'][0]['text'].strip())
            # self.ui.CodeChatGPTOutput.setPlainText(output)oices' in response:
            #             #     return response['choices'][0]['text'].strip()
            #             # else:
            #             #     return None
            # if response and 'ch
            output = response['choices'][0]['text'].strip()
            token = len(input_text) + len(output)
            print("4/2", output)
            # output = exec(output)
            print("4/3", output)
            self.ui.tableChatGPTOutput.setPlainText(output)
            self.ui.tableChatGPTOutput.setText(str(token))
            # self.ui.CodeChatGPTOutput.setPlainText(response['choices'][0]['text'].strip())
            # self.ui.CodeChatGPTOutput.setPlainText(response['choices'][0]['text'].strip())

        except:
            self.ui.tableChatGPTOutput.setStyleSheet("color: red")
            self.ui.tableChatGPTOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!")
            print("Anfrage konnte nicht gesendet werden!")


    def closeEvent(self, event):
        main_window.show()

class ProjektteamFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Projektteam()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - Projektteam")

    def closeEvent(self, event):
        main_window.show()




class FirstRowChatGPTFenster(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FirstRowChatGPT()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Bilder/Icon_Info.svg"))
        self.setWindowTitle("INFOMOTION - FirstRow ChatGPT")

        self.ui.pushButton.clicked.connect(self.process_input)

    def process_input(self):
        # Setze deine OpenAI API-Zugriffsschlüssel
        # openai.api_key = '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'

        input_text = self.ui.firstRowChatGPTInput.toPlainText()
        first_row = pd.read_csv(main_window.pfad).columns.tolist()

        print("Erste Reihe: ",first_row)
        # if main_window.pfad != None:
        #     input_text = "schreib python Code um aus einer Tabelle folgende Frage zu lesen."+self.input_text_edit.toPlainText() + " aus der Tabelle mit dem Pfad: "+main_window.pfad
        # else:
        #     input_text = self.input_text_edit.toPlainText()

        # Hier kannst du deinen Code zum Senden der Eingabe an ChatGPT und zum Empfang
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=input_text,
                max_tokens=250,  # Anzahl der Tokens in der Antwort
                temperature=0.7,  # Steuerung der Antwortvarianz
                n=1,  # Anzahl der Antworten, die zurückgegeben werden sollen
                stop=None,  # Hier kannst du eine benutzerdefinierte Stop-Bedingung angebe
            )

            self.ui.firstRowChatGPTOutput.setPlainText(response['choices'][0]['text'].strip())
        except:
            self.ui.firstRowChatGPTOutput.setStyleSheet("color: red")
            self.ui.firstRowChatGPTOutput.setPlainText("Error: Anfrage konnte nicht gesendet werden!")
            print("Anfrage konnte nicht gesendet werden!")
        # if main_window.pfad != None:
        #     # output=exec(response['choices'][0]['text'].strip())
        #     self.output_text_edit.setPlainText(response['choices'][0]['text'].strip())
        #
        # else:
        #     self.output_text_edit.setPlainText(response['choices'][0]['text'].strip())




    def closeEvent(self, event):
        main_window.show()





app = QApplication(sys.argv)
print(app, "app")
main_window = MainWindow()
# window=direktChatGPT()
main_window.show()
sys.exit(app.exec_())
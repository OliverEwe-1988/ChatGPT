import pandas as pd 

#Lese Daten aus CSV-Datei
SummerwineTest = pd.read_csv("D:/Entwicklung/InfomotionChatGPT/SummerwineTest.csv") 

#Berechne die Anzahl der Rebsorten
AnzahlRebsorten = len(SummerwineTest['Rebsorten'].unique()) 

print('Es gibt ' + str(AnzahlRebsorten) + ' Rebsorten aus der Tabelle.')
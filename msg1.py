import requests
import serial
import time

# Conexão com a porta serial do Arduino
arduino = serial.Serial('COM3', 9600)

ultimo_estagio = None

url = "http://127.0.0.1:8080/message/sendText/arduino"

headers = {
    "apikey": "1234",
    "Content-Type": "application/json"
}

while True:
    if arduino.in_waiting:
        
        linha = arduino.readline().decode().strip()
        print("Linha recebida:", linha)
        try:
            tensao = float(linha)
            print("Tensão:", tensao)

            # Estágio 1
            if tensao < 1.5 and ultimo_estagio != 1:
                payload = {
                    "number": "5521996027033",
                    "textMessage": {"text": "Arroz"}
                }
                response = requests.post(url, json=payload, headers=headers)
                print(response.text)
                ultimo_estagio = 1

            # Estágio 2
            elif tensao < 3 and ultimo_estagio != 2:
                payload = {
                    "number": "5521996027033",
                    "textMessage": {"text": "Feijão"}
                }
                response = requests.post(url, json=payload, headers=headers)
                print(response.text)
                ultimo_estagio = 2

            # Estágio 3
            elif ultimo_estagio != 3:
                payload = {
                    "number": "5521996027033",
                    "textMessage": {"text": "Purê"}
                }
                response = requests.post(url, json=payload, headers=headers)
                print(response.text)
                ultimo_estagio = 3

        except ValueError:
            print("Erro ao converter tensão")
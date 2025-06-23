const int botaoPin = 8; // Pino onde o botão está conectado
const int potPin = A5; //Pino do potenciometro
bool estadoAnteriorBotao = HIGH;

void setup() {

  pinMode(botaoPin, INPUT_PULLUP); // Ativa resistor pull-up interno
  Serial.begin(9600);              // Inicia comunicação serial

}

void loop() {
  bool estadoAtualBotao = digitalRead(botaoPin);
 
if (estadoAnteriorBotao == HIGH && estadoAtualBotao == LOW) {
    int valorAnalogico = analogRead(potPin);
    float voltagem = valorAnalogico * (5.0 / 1023.0);
    Serial.println(voltagem);
    delay(300);
  } 

  estadoAnteriorBotao = estadoAtualBotao;

  delay(300); // Espera 300ms para evitar mensagens rápidas demais
}

const int fsrPin = A0;  // Pin analógico donde está conectado el FSR

void setup() {
  Serial.begin(9600);  // Iniciar la comunicación serie a 9600 bps
  pinMode(fsrPin, INPUT);
}

void loop() {
  int fsrValue = analogRead(fsrPin);  // Leer el valor del FSR
  Serial.println(fsrValue);  // Enviar el valor del FSR a través de la serie
  delay(100);  // Esperar 100 ms antes de la siguiente lectura
}

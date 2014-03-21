// AI : ANALOG INPUT
// DI : DIGITAL INPUT
// DO : DIGITAL OUPUT

#include <DHT.h>

#define PHOTOCELL_AI A0
#define MOISTURE_AI A1
#define WATER_EMPTY_AI A2
#define WATER_FULL_AI A3

#define DHT_DI 2
#define RELAY_DO 3
#define WATER_LED_DO 4

#define WATER_ON 0
#define WATER_OFF 1

#define TEMPERARTURE_CMD 2
#define HUMIDITY_CMD 3
#define LIGHT_CMD 4
#define SOIL_CMD 5 
#define WATER_CMD 6

#define INFO_CMD 7

// Setting up the DHTxx library
#define DHT_TYPE DHT11   

DHT dht(DHT_DI, DHT_TYPE);

//-------------------------------------
//              INPUTS
//-------------------------------------
int getHumidity() {
  //float humidity = dht.readHumidity();
  int humidity = analogRead(DHT_DI);
  if(isnan(humidity)) {
    return -1;
  }  
  //Serial.print("Humidity: "); 
  //Serial.print(humidity);
  //Serial.println(" %");
  return humidity;
}

int getTemperature() {
  float temperature = dht.readTemperature(false);
  if(isnan(temperature)) {
    return -1;
  }
  //Serial.print("Temperature: "); 
  //Serial.print(temperature);
  //Serial.println(" ºC");  
  return temperature;
}

int getSoilMoisture() {
  int moisture = analogRead(MOISTURE_AI);
  //Serial.print("Soil moisture: ");
  //Serial.println(moisture);
  return moisture;
}

int getBrightness() {
  int reading = analogRead(PHOTOCELL_AI);
  // LED gets brighter the darker it is at the sensor
  reading = 1023 - reading;
  //Mapping to 0-255
  int brigthtness = map(reading, 0, 1023, 0, 255);
  //Serial.print("Brightness : ");
  //Serial.println(reading);     // the raw analog reading 
  return brigthtness;
}

int getWaterLevel() {
   int reading = analogRead(WATER_EMPTY_AI);
   //Serial.print("Water level: ");
   //Serial.println(reading);
   return reading;
}

boolean isTankEmpty() {
  if(analogRead(WATER_FULL_AI) == 0) {
    return false;
  } else {
    return true;
  }
}


//-------------------------------------
//              OUTPUTS
//-------------------------------------

void setWatering(boolean state) {
  if(state) {
    digitalWrite(RELAY_DO, HIGH);  
  } else {
    digitalWrite(RELAY_DO, LOW);  
  }
}


void setEmptyTank(boolean state) {
  if(state) {
    digitalWrite(WATER_LED_DO, HIGH);  
  } else {
    digitalWrite(WATER_LED_DO, LOW);  
  }    
}

//-------------------------------------
//          SETUP AND LOOP
//-------------------------------------

int readCommand() {
  if (Serial.available() > 0) {
      return Serial.read(); 
  }
  return -1;
}

void execCommand(int cmd, String &infos) {
  if(cmd == WATER_ON) {
      setWatering(true);  
  } else if (cmd == WATER_OFF) {
      setWatering(false);
  } else if (cmd == TEMPERARTURE_CMD) {
      infos = String(getTemperature());    
  } else if (cmd == HUMIDITY_CMD) {
      infos = String(getHumidity());
  } else if (cmd == LIGHT_CMD) {
      infos = String(getBrightness());   
  } else if (cmd == SOIL_CMD) {
      infos = String(getSoilMoisture());
  } else if (cmd == WATER_CMD) {
      infos = String(getWaterLevel());
  } else {
      //Waiting for the DHT11 to return :)
      //infos = String(getTemperature()) + "|" + String(getHumidity()) + "|" + String(getBrightness()) + "|" + String(getSoilMoisture()) + "|" + String(getWaterLevel());
      infos = String(20) + "|" + String(50) + "|" + String(getBrightness()) + "|" + String(getSoilMoisture()) + "|" + String(getWaterLevel());
  } 
}


String infos;
void loop () {
  int cmd = readCommand();
  if(cmd != -1) {
    execCommand(cmd,infos);
    Serial.println(infos);
  }
  //Checking that water tank is not full
  setEmptyTank(isTankEmpty());
}

void setup (){

  digitalWrite(RELAY_DO, LOW);
  pinMode(RELAY_DO, OUTPUT);
  pinMode(WATER_LED_DO, OUTPUT);

  pinMode(MOISTURE_AI, INPUT);
  pinMode(PHOTOCELL_AI, INPUT);
  pinMode(WATER_EMPTY_AI, INPUT);
  pinMode(WATER_FULL_AI, INPUT);
  
  pinMode(DHT_DI, INPUT);
    
  Serial.begin(9600);
  //dht.begin();
  
  infos.reserve(25);
  infos = "";
}

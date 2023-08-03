#include <SPI.h>
#include <WiFiNINA.h>

// Setting information about the Wi-Fi network
char ssid[] = "YourWiFiNetwork";
char password[] = "YourWiFiPassword";

// Set the port number of the server
int serverPort = 1234;

WiFiServer server(serverPort);

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    // Wait for the serial port to connect
  }

  // Initialize the Wi-Fi module
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    while (true);
  }

  // Connect to the Wi-Fi network
  while (WiFi.begin(ssid, password) != WL_CONNECTED) {
    Serial.println("Connecting to WiFi...");
    delay(1000);
  }

  // Start the server
  server.begin();
  Serial.println("Server started.");
}

void loop() {
  // Waiting for clients to connect
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Client connected.");

    // Read the data sent by the client
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        // Process received data here
        // ...
        Serial.write(c); // Example: Displaying data back to the serial port
      }
    }

    client.stop();
    Serial.println("Client disconnected.");
  }
}
import React, { useEffect } from 'react';
import { View, Text } from 'react-native';
import * as Location from 'expo-location';
import io from 'socket.io-client';

const socket = io("http://YOUR_SERVER_IP:5000"); // replace YOUR_SERVER_IP

export default function App() {
  useEffect(() => {
    const startTracking = async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') return;

      // Background/foreground watch
      Location.watchPositionAsync(
        { accuracy: Location.Accuracy.Highest, timeInterval: 5000, distanceInterval: 5 },
        (loc) => {
          socket.emit("location_update", {
            doctor_id: 1,
            name: "Dr. Strange",
            latitude: loc.coords.latitude,
            longitude: loc.coords.longitude
          });
        }
      );
    };

    startTracking();
  }, []);

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Doctor live tracking running...</Text>
    </View>
  );
}

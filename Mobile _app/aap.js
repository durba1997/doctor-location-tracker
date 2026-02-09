import React, { useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import io from 'socket.io-client';

const socket = io("http://YOUR_SERVER_IP:5000"); // Replace with backend IP

// Define 3–5 fake doctors
const doctors = ["doctor_fake_1", "doctor_fake_2", "doctor_fake_3", "doctor_fake_4", "doctor_fake_5"];

export default function App() {

  useEffect(() => {
    // Send location for all doctors every 5 seconds
    const interval = setInterval(() => {
      doctors.forEach((id) => {
        const fakeLat = 20 + Math.random();  // random latitude
        const fakeLon = 77 + Math.random();  // random longitude
        socket.emit("location_update", { id, lat: fakeLat, lon: fakeLon });
        console.log(`Sent location for ${id}: ${fakeLat}, ${fakeLon}`);
      });
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <View style={{ padding: 50 }}>
      <Text>Multi-Doctor Simulator Running</Text>
      {doctors.map((id) => (
        <Button key={id} title={`Send one-time location for ${id}`} onPress={() => {
          const fakeLat = 20 + Math.random();
          const fakeLon = 77 + Math.random();
          socket.emit("location_update", { id, lat: fakeLat, lon: fakeLon });
        }} />
      ))}
    </View>
  );
}

import React, { useEffect } from "react";
import { View, Text, StyleSheet, ScrollView } from "react-native";
import io from "socket.io-client";

// 🔁 CHANGE THIS IF BACKEND IS ON ANOTHER MACHINE
const socket = io("http://localhost:5000");

// 👨‍⚕️ Fake doctors list (3–5)
const doctors = [
  "doctor_fake_1",
  "doctor_fake_2",
  "doctor_fake_3",
  "doctor_fake_4",
  "doctor_fake_5",
];

export default function App() {
  useEffect(() => {
    console.log("Fake Doctor App Started");

    // Send fake locations every 5 seconds
    const interval = setInterval(() => {
      doctors.forEach((id) => {
        const fakeLat = 20 + Math.random(); // India-like latitude
        const fakeLon = 77 + Math.random(); // India-like longitude

        socket.emit("location_update", {
          id: id,
          lat: fakeLat,
          lon: fakeLon,
        });

        console.log(`📍 ${id} -> ${fakeLat}, ${fakeLon}`);
      });
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🧑‍⚕️ Fake Doctor Simulator</Text>
      <Text style={styles.subtitle}>
        Sending live locations for multiple doctors
      </Text>

      {doctors.map((doc) => (
        <Text key={doc} style={styles.doctor}>
          ✅ {doc} is sending location
        </Text>
      ))}

      <Text style={styles.note}>
        Stop the app to simulate doctors going offline.
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 40,
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    marginBottom: 20,
    color: "gray",
  },
  doctor: {
    fontSize: 16,
    marginVertical: 5,
  },
  note: {
    marginTop: 30,
    fontSize: 14,
    color: "gray",
  },
});

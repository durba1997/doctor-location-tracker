// Connect to backend
const socket = io("http://localhost:5000");

// Initialize map
const map = L.map("map").setView([22.5726, 88.3639], 5); // India center

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

let doctorMarkers = {};

// Receive live updates
socket.on("location_broadcast", (locations) => {
  for (let id in locations) {
    const loc = locations[id];

    if (doctorMarkers[id]) {
      // Move existing marker
      doctorMarkers[id].setLatLng([loc.latitude, loc.longitude]);
    } else {
      // Create new marker
      doctorMarkers[id] = L.marker([loc.latitude, loc.longitude])
        .addTo(map)
        .bindPopup(`Doctor ID: ${id}`);
    }
  }
});

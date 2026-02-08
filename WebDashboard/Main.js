const socket = io("http://YOUR_SERVER_IP:5000"); // backend server IP
let map;
let markers = {};

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 20.5937, lng: 78.9629}, // India center
        zoom: 5
    });
}
initMap();

// Update marker when live location comes
socket.on("location_broadcast", data => {
    const pos = {lat: data.latitude, lng: data.longitude};
    const color = data.online ? "green" : "gray";

    if (markers[data.doctor_id]) {
        markers[data.doctor_id].setPosition(pos);
        markers[data.doctor_id].setIcon(getMarkerIcon(color));
    } else {
        markers[data.doctor_id] = new google.maps.Marker({
            position: pos,
            map: map,
            label: data.name,
            icon: getMarkerIcon(color)
        });
    }
});

// Optional: change offline markers every 10s
setInterval(() => {
    fetch("http://YOUR_SERVER_IP:5000/last_seen")
        .then(res => res.json())
        .then(data => {
            for (const id in data) {
                const doc = data[id];
                if (markers[id]) {
                    const color = doc.online ? "green" : "gray";
                    markers[id].setIcon(getMarkerIcon(color));
                }
            }
        });
}, 10000);

// Helper: colored marker icon
function getMarkerIcon(color) {
    return {
        path: google.maps.SymbolPath.CIRCLE,
        scale: 10,
        fillColor: color,
        fillOpacity: 1,
        strokeWeight: 1,
        strokeColor: "white"
    };
}

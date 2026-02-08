const socket = io("http://YOUR_SERVER_IP:5000");
let map;
let markers = {};

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 20.5937, lng: 78.9629}, // India center
        zoom: 5
    });
}
initMap();

socket.on("location_broadcast", data => {
    const pos = {lat: data.latitude, lng: data.longitude};
    if (markers[data.doctor_id]) {
        markers[data.doctor_id].setPosition(pos);
    } else {
        markers[data.doctor_id] = new google.maps.Marker({
            position: pos,
            map: map,
            label: data.name
        });
    }
});

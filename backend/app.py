from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Store live doctor locations in memory
doctor_locations = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    doctor_id = data.get('doctor_id')
    lat = data.get('lat')
    lon = data.get('lon')
    if doctor_id and lat and lon:
        doctor_locations[doctor_id] = {'lat': lat, 'lon': lon}
        socketio.emit('locations_update', doctor_locations)
        return {'status': 'success'}, 200
    return {'status': 'fail', 'message': 'Invalid data'}, 400

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

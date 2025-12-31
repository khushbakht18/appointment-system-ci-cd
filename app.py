from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage
appointments = []

# Create appointment
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointments.append(data)
    return jsonify({"message": "Appointment created successfully"}), 201

# View appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(debug=True)
import firebase_admin
from firebase_admin import credentials, db
from fbk import fbk_dict

# Initialize Firebase Admin SDK
cred = credentials.Certificate(fbk_dict)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://yellow-vortex-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get Firebase Realtime Database references
commands_ref = db.reference('/commands')
bpm_ref = commands_ref.child('BPM')
ECG_ref = commands_ref.child('ECG')
directionRef = commands_ref.child('Drive').child('command')



def set_bpm(bpm):
    bpm_ref.set({
        'average_bpm': bpm
    })

def set_ECG(ecg):
    ECG_ref.set({'average_ecg': ecg})

def set_humidity(humidity):
    commands_ref.update({"humidity": humidity})

def set_temperature(temperature):
    commands_ref.update({"temperature": temperature})


async def get_direction():
    direction = directionRef.get()
    return direction


def update_all(temperature, humidity, ecg, bpm):
    commands_ref.update({
        "temperature": temperature,
        "humidity": humidity,
        "ECG": {'average_ecg': ecg},
        "BPM": {'average_bpm': bpm}
    })
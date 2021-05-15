import firebase_admin
from firebase_admin import credentials, db
import math

cred = credentials.Certificate("example-95f12-firebase-adminsdk-ydwjg-d041a9e9ec.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://example-95f12-default-rtdb.firebaseio.com/'
})

#adding information 
ref = db.reference("/")

new_person = {}
new_person['name'] = input("name: ")
new_person['lat'] = float(input("Latitude: "))
new_person['long'] = float(input("Longitude: "))

ref.child('people').push(new_person)


#updating information
ref = db.reference("/people/-M_iKCv8w1ta7jXHMrJ7") 
ref.update({"lat": 14})

#retrieving information
ref = db.reference("/people/-M_iKCv8w1ta7jXHMrJ7")
print(ref.child("name").get())

#deleting information
ref = db.reference("/people/-M_iKCv8w1ta7jXHMrJ7")
ref.set({})

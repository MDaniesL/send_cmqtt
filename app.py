import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform
from PIL import Image

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="157.230.214.127"
port=1883
client1= paho.Client("CLIENT555")
client1.on_message = on_message



st.title("Control de Rueda")

st.subheader("El mapache ladrón quiere abrir la caja fuerte, pero necesita tu ayuda para decifrar la combinación correcta. Experimenta rotando a diferentes ángulos para darle ideas.")

image = Image.open('Sly.png')
st.image(image, width=500)

if st.button('Set a 100.00'):
    act1="ON"
    client1= paho.Client("CLIENT555")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("CLIENT555", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Set a 0.00'):
    act1="OFF"
    client1= paho.Client("CLIENT555")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("CLIENT555", message)
  
    
else:
    st.write('')

values = st.slider('Mueve a un ángulo específico',0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    client1= paho.Client("CLIENT555")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("CLIENT555", message)
    
 
else:
    st.write('')





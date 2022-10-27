  import time
import threading
import os
import itertools
from threading import Thread,Semaphore
import queue
from edge_impulse_linux.runner import ImpulseRunner
import signal

import json

import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from email.message import EmailMessage
from datetime import datetime
import time as t
import smtplib


cont = 0
#import pdb;pdb.set_trace()

semaforo = Semaphore(1);
model_queue = queue.Queue()

def Recibe():
    def customCallback(client,userdata,message):
        print("callback came...")
        print(message.payload)
       
        a=message.payload.decode()
        semaforo.acquire();    
        f=open("datos.txt","a")
        f.write(a)
        f.close()
        semaforo.release();
        time.sleep(1)

    from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

    myMQTTClient = AWSIoTMQTTClient("RPI Gateway")
    myMQTTClient.configureEndpoint("a1zfogi5kom6d2-ats.iot.us-east-1.amazonaws.com", 8883)
    myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./4289199d9175c33d237d27b9856a6f7dfcf546fea6a78a1e8ec0f3b7f4c507a8-private.pem.key", "./4289199d9175c33d237d27b9856a6f7dfcf546fea6a78a1e8ec0f3b7f4c507a8-certificate.pem.crt")

    myMQTTClient.connect()
    print("Client Connected")

    myMQTTClient.subscribe("esp32/message", 1, customCallback)
    print('waiting for the callback. Click to conntinue...')
    x = input()
    print(x)
   


    myMQTTClient.unsubscribe("esp32/pub")
    print("Client unsubscribed")


    myMQTTClient.disconnect()
    print("Client Disconnected")
   
def Manejoarchivo():
 
    def Last(fname, N):
    # opening file using with() method
    # so that file get closed
    # after completing work
        with open(fname) as file:
           
            x=[]
            # loop to read iterate
            # last n lines and print it
            for line in (file.readlines() [-N:]):
               
                x.append(line.strip('\n').split(','))
               
            flat_list = itertools.chain(*x)    
            flat_list=list(flat_list)
           
           
           
            for i in range(len(flat_list)):
                flat_list[i] = int(flat_list[i])
            return flat_list
         
           
           
    ultimo=[]        

    while 1:
       
        if(os.path.exists('datos.txt')):
               
            semaforo.acquire();
           
            datos=Last('datos.txt', 6)
            semaforo.release();
       
           
            time.sleep(1)
           
            if ultimo == datos:
                pass
               
            else:
                ultimo=datos
                model_queue.put(ultimo)
                time.sleep(1)
                               
        else:
            print("no hay sudicientes datos")
            time.sleep(1)
           
           
def modelo():
       
   
    def enviomqtt(westimacion):
        global cont
       
        mensaje = "Alerta opcupacion"
        ENDPOINT = "a1zfogi5kom6d2-ats.iot.us-east-1.amazonaws.com"
        CLIENT_ID = "a1b23cd45e"
        RANGE = 20
     
        print('Begin Publish')
        print(westimacion)
        wfecha = datetime.now()
        w2fecha = wfecha.strftime("%Y-%m-%d-%H:%M:%S")
        print(w2fecha)
        for i in range (1):
         
            data= {

          "IdEspacio": "1",

          "Fecha": w2fecha,

          "Ocupacion":  westimacion

         

        }
        vlocar = cont
        vlocar = vlocar+1
        cont= vlocar
        print(cont)
               
        if cont >=6 :
            print("publica ocupacion")
            myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
            myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
            myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
            myAWSIoTMQTTClient.connect()
            message = {"message" : data}
            print(message)
            myAWSIoTMQTTClient.publish(TOPIC, json.dumps(data), 0)
            print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
            t.sleep(0.1)
            print('Publish End')
       
            mensaje=("Alerta espacio 1"+ " " +"ocupacion" + " " +westimacion )
            print(mensaje)
            email.set_content(mensaje)
            smtp = smtplib.SMTP_SSL("smtp.gmail.com")
            smtp.login(remitente, "wxnfxquaruumlmqx")
            smtp.sendmail(remitente, destinatario, email.as_string())
            smtp.quit()
           
       
             

       
     
     
 
 
 
    model = "Pruebadownload.eim"
    dir_path = os . path . dirname ( os . path . realpath ( __file__ ) )  
    modelfile = os . path . join ( dir_path , model )

    while 1:

        if model_queue.empty():
           
            time.sleep(0.2)

        else:

            features = model_queue.get()
            print(features)
#print(features)
             
            print('MODEL: ' + modelfile)
            modelfile="/home/tamayoa/modelfile.eim"
            PATH_TO_ROOT = "./AmazonRootCA1.pem"
            PATH_TO_KEY = "./4289199d9175c33d237d27b9856a6f7dfcf546fea6a78a1e8ec0f3b7f4c507a8-private.pem.key"
            PATH_TO_CERT = "./4289199d9175c33d237d27b9856a6f7dfcf546fea6a78a1e8ec0f3b7f4c507a8-certificate.pem.crt"
            TOPIC = "iot/testing"
            try:
              model_info = runner.init()
              print("entro")
             
             
              res = runner.classify(features)
              classification = res ["result"]
                 
              print(classification)
               
              print(type(classification))
              print(classification['classification']['Alta'])
              print(classification['classification']['Media'])
              print(classification['classification']['Baja'])
                 
              v1 = classification['classification']['Alta']
              v2 = classification['classification']['Media']
              v3 = classification['classification']['Baja']
                 
              if v1 >= v2 and v1 >= v3:
                 print("ocupacion Alta")
                 enviomqtt("Alta")
                 time.sleep(1)
              elif v2 >= v1 and v2>= v3:
                 print("ocupacion Media")
                 enviomqtt("Media")
                 time.sleep(1)
              elif v3 >= v1 and v3>= v2:
                 print("ocupacion  Baja")
                 enviomqtt("Baja")
                 time.sleep(1)
              else:
                 print("error")
                 time.sleep(1)

   
            finally:
              if (runner):
                  runner.stop()                            
            time.sleep(1)
def Main():
   
   
    global remitente
    remitente = "andretama1010@gmail.com"
    global destinatario
    destinatario = "andretama1010@hotmail.com"
    global mensaje    
    mensaje = "Alerta opcupacion"
    global email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Correo de prueba"
    global runner
    runner= None
    modelfile="/home/tamayoa/modelfile.eim"
    runner = ImpulseRunner(modelfile)
    model_info = runner.init()
    def signal_handler(sig, frame):
        print('Interrupted')
        if (runner):
            runner.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    def help():
        print('python classify.py Pruebadownload.eim <path_to_model.eim> <path_to_features.txt>')

    def ppal(argv):
        try:
            opts, args = getopt.getopt(argv, "h", ["--help"])
        except getopt.GetoptError:
            help()
            sys.exit(2)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                help()
                sys.exit()

        if len(args) <= 1:
            help()
            sys.exit(2)

        model = args[0]


        features_file = io.open(args[1], 'r', encoding='utf8')
        features = features_file.read().strip().split(",")
        if '0x' in features[0]:
            features = [float(int(f, 4)) for f in features]
        else:
            features = [float(f) for f in features]


        dir_path = os.path.dirname(os.path.realpath(__file__))
        modelfile = os.path.join(dir_path, model)

       
        runner = ImpulseRunner(modelfile)
           
       
        try:
            print("Entro")
            model_info = runner.init()
            print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
            #features=
            #res = runner.classify(features)
            #print("classification:")
            #print(res["result"])
            #print("timing:")
            #print(res["timing"])

        finally:
            if (runner):
                runner.stop()
   
   
   
    threading.Thread(target=Recibe).start()
    threading.Thread(target=Manejoarchivo).start()    
    threading.Thread(target=modelo).start()  

Main()

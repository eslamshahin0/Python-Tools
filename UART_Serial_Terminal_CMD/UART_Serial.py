import serial
#if you don't have the library open cmd and write <pip install PySerial>

""""put your avilable COM port name here and make sure 
that is not opened by another program and the same baud rate""".

ser = serial.Serial("COM5",9600)

#Function to send some text with "\r\n"
def send_text(text):
    text=text+"\r\n"
    #encode data before sending
    ser.write(text.encode())
    
#Function to recive string  without polling till "\r\n"
def recive_text():
    #check if there are comming chars 
    if(ser.inWaiting()==1):
        rec=ser.readline()  #read till \r\n
        rec=rec.decode()    #decode the recived data
        print ("Recived : " , rec)  #printing data into cmd
	
#Function wait for string by polling till "\r\n"
def recive_textpoll():
    
    while(ser.inWaiting()==0):
        pass    #do nothong
    rec=ser.readline()
    rec=rec.decode()
    print ("Recived : " , rec)
    
while(1):
    #data = input("Enter Text To Send : ")
    #send_text(data)
    recive_textpoll()

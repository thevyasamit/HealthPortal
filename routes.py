from flask import Flask, render_template,request,flash,redirect, jsonify, url_for
import csv 
import pymongo
import serial
import time, uuid
import pyaudio, wave


client = pymongo.MongoClient('mongodb://10.6.0.179:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
db = client.healthDB

# client = pymongo.MongoClient('localhost',27017)
# db = client.healthDB





app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
@app.route("/home/", methods = ['POST','GET'])
def gohome():
	return render_template('home.html')


@app.route("/patient-info/", methods=['POST', 'GET'])
def goPatient():
	return render_template('send.html')

@app.route("/doctor-page/",  methods = ['POST', 'GET'])
def goDoc():
	return render_template('data.html')


@app.route("/send/", methods=['POST','GET'])
def userData():
	#sensorData = getSensorData()
	iD = uuid.uuid4()
	print(request.form)
	ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
	time.sleep(2)
	sensorData =[]                       
	for i in range(2,10):
		b = ser.readline()         
		string = b.decode()  
		string = string.rstrip()
    	#flt = float(string)        
    	#print(string)
		sensorData.append(string)          
		time.sleep(1)            
	ser.close()

	# Code for recording heart beats
	time.sleep(1)
	CHUNK = 2024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 10
	WAVE_OUTPUT_FILENAME = str(iD)+".wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(r"/Users/avyas/Desktop/teleMed/flaskDev/flaskCode/static/audio/"+WAVE_OUTPUT_FILENAME,"wb")
	#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	# return sensorData
	user = {
		"_id" : iD,
		"name": request.form.get('name'),
		"contact": request.form.get('contact'),
		"age" : request.form.get('age'),
		"gender" : request.form.get('gender'),
		"sensor" : sensorData,
		"audio" : WAVE_OUTPUT_FILENAME

	}
	db.users.insert_one(user)
	return render_template('home.html')


@app.route("/data/", methods = ['POST','GET'])
def usr_data():
	data = []
	data = db.users.distinct('contact')
	#data = db.users.find({} , { "name" : 1 , "_id" : 0})
	#data = db.users.find()
	return render_template('data.html',data = data)



@app.route("/info/", methods =['POST','GET'])
def info():
	if request.method == 'POST':
		data = []
		con =request.form.get('val')
		data = db.users.find({ "contact" : con }, {"_id" : 1, "name" : 1, "contact" : 1 , "age" : 1, "sensor" : 1 , "audio" :1})
		# print(con)
		# nm =request.form.get('val2')
		# data = db.users.find({ "name" : nm }, {"_id" : 1, "name" : 1, "contact" : 1 , "age" : 1, "sensor" : 1})
		
		# print(nm)
		return render_template('recieve.html', data = data)
	else:
		# gname = request.args.get('nm')
		# #print(gname)
		return render_template('recieve.html')


@app.route('/info/<path:filename>', methods=['POST','GET'])
def filename(filename):
	print("The filename is : ", filename)
	chunk = 1024  
	audioFname= filename
	#open a wav format music  
	f = wave.open(r"/users/avyas/Desktop/teleMed/flaskDev/flaskCode/static/audio/"+audioFname,"rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  

	#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  
	return ('', 204)

# @app.route("/play_audio/", methods = ['POST', 'GET'])
# def play_audio():
# 	if request.method == 'POST':
# 		f = request.form.get('audio')
# 	else:
# 		f = request.args.get('audio')
	# chunk = 1024  
	# audioFname= '59ffc94a-4dfd-4012-a24e-97906d5609f4.wav'
	# #open a wav format music  
	# f = data#wave.open(r"/users/avyas/Desktop/teleMed/flaskDev/flaskCode/"+audioFname,"rb")  
	# #instantiate PyAudio  
	# p = pyaudio.PyAudio()  
	# #open stream  
	# stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	#             channels = f.getnchannels(),  
	#             rate = f.getframerate(),  
	#             output = True)  
	# #read data  
	# data = f.readframes(chunk)  

	# #play stream  
	# while data:  
	# 	stream.write(data)  
	# 	data = f.readframes(chunk)  

	# #stop stream  
	# stream.stop_stream()  
	# stream.close()  

	# #close PyAudio  
	# p.terminate()
	# 	print(f)
	# return render_template()

@app.route("/recieve/")
def recieve():
	return render_template('recieve.html')

if __name__ == "__main__":
	app.run()




# - tell isp to open port
# - portname :tcp 80 443 3478 3479 3480
# 			udp 3478 3479
# - Reliance 

# In order to run this app uisng environment variable use 
# Use this command in terminal: 
# export FLASK_APP = try.py (filename in which flask is imported with .py extension.)
# in order to not run server again and again use export FLASK_DEBUG =1 or in app.run(debug = true)
# export FLASK_ENV=development worked for enabling debug mode in my case

#MongoDB commands
#brew services start mongodb-community
#brew services stop mongodb-community



#helpful links
#1. https://stackoverflow.com/questions/28336163/how-to-connect-robomongo-to-mongodb
#2. https://thedatafrog.com/en/articles/mongodb-remote-raspberry-pi/
#3. https://stackoverflow.com/questions/55376274/connect-and-allow-multiple-ips-for-mongodb-accepting-connections
#4. For Windows netsh firewall configuration:- https://docs.mongodb.com/manual/tutorial/configure-windows-netsh-firewall/
#5. https://mkyong.com/mongodb/mongodb-allow-remote-access/

#Libreria PyAudio
import pyaudio
#Libreria para los formatos de sonido
import wave

FORMAT = pyaudio.paInt16
#Cada frame tiene 2 samples por eso channels es igual a 2
CHANNELS = 2
#Es el numero de frames en el buffer
CHUNK = 1024
#Numero de samples recogidos por segundo
RATE = 44100
#Segundos de la grabacion
RECORD_SECONDS = 10
#Nombre del archivo de la grabacion
WAVE_OUTPUT_FILENAME = "AudioGrabado.mp3"

#Instancia pyaudio
p = pyaudio.PyAudio()

#Comienza la grabacion con los parametros inicializados anteriormente
stream = p.open(format=FORMAT,
			channels = CHANNELS,
			rate=RATE,
			input=True,
			frames_per_buffer=CHUNK)

print("Tu audio esta siendo grabado :)")

frames = []
#Grabacion del audio desde 0 hasta el tamanio establecido
for i in range(0,int(RATE/CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	frames.append(data)
#Fin de bucle e imprimimos por pantalla que la grabacion ha acabado
print("Fin de la grabacion")
#El stream termina y pyaudio tambien termina
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

import pyaudio
from pywt import wavedec
import numpy as np
import pywt as wt
import sys
import audioop
import itertools
import math
from collections import Counter
from sys import maxsize
from ctypes import c_int32
from pyaudio import paInt16

x = np.random.rand(512)
coefs = wavedec(x, 'db1',level=5)


chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1	
CHUNK = 1024
RATE = 44100
RECORD_SECONDS = 5
WIDTH = 2
data = []
ITERACIONESDWT = 9

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)


while True:
	data = stream.read(CHUNK)
	stream.write(data, chunk)


#Metodo entropia
#def entropy(labels): 
    prob_dict = {x:labels.count(x)/len(labels) for x in labels} 
    probs = np.array(list(prob_dict.values())) 

    return - probs.dot(np.log2(probs)) 

#Calculo maximo
#def maximo(array):
    max = 0
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
    return max


#Calculo minimo
#def minimo(arr):
    min = 0
    for i in range(len(arr)):
        if arr[i]<min:
            min=array[i]
    return min
	
	 

#Metodo main
def main():
    minimo(cA.min)

if __name__ == '__main__':
    
main()


stream.stop_stream()
stream.close()

p.terminate()



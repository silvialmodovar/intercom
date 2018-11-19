# PyAudio to capture and broadcast audio
import pyaudio
# NumPy to change variable types
import numpy as np
# Pywt to calculate Discrete Wavelet Transform (DWT)
import pywt
# SciPy to calculate entropy
import scipy.stats as st
import sys


# Declaration of variables
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

# Variable that we use to capture and broadcast audio
stream = p.open(format=p.get_format_from_width(2),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)


# Main
def main():
      i = 0
      while True:
            i = i+1
            # Read from the sound card Chunk to CHUNK
            data = stream.read(CHUNK)
            sys.stderr.write(".")
            sys.stderr.flush()
            # Pass from type bytes to int16 using the numpy library
            array_In = np.frombuffer(data, dtype=np.int16)
            # Hacemos la transformada
            coeffs = pywt.wavedec(array_In, 'db1', level=5)
            a = coeffs
            # Para acceder a los planos de bits de un array de enteros, creamos un array:
            a = np.array(array_In, dtype=np.int32)
            b0 = a.astype(np.int32) & 0b1                  # Primer plano de bits (LSB) del array a
            b1 = (a & (0b1<<1)).astype(np.int32) >> 1      # Segundo plano de bits de a
            b2 = (a & (0b1<<2)).astype(np.int32) >> 2      # Tercer plano
            b3 = (a & (0b1<<3)).astype(np.int32) >> 3
            b4 = (a & (0b1<<4)).astype(np.int32) >> 4
            b5 = (a & (0b1<<5)).astype(np.int32) >> 5
            b6 = (a & (0b1<<6)).astype(np.int32) >> 6
            b7 = (a & (0b1<<7)).astype(np.int32) >> 7
            b8 = (a & (0b1<<8)).astype(np.int32) >> 8
            b9 = (a & (0b1<<9)).astype(np.int32) >> 9
            b10 = (a & (0b1<<10)).astype(np.int32) >> 10
            b11 = (a & (0b1<<11)).astype(np.int32) >> 11
            b12 = (a & (0b1<<12)).astype(np.int32) >> 12
            b13 = (a & (0b1<<13)).astype(np.int32) >> 13
            b14 = (a & (0b1<<14)).astype(np.int32) >> 14
            b15 = (a & (0b1<<15)).astype(np.int32) >> 15
            b16 = (a & (0b1<<16)).astype(np.int32) >> 16
            b17 = (a & (0b1<<17)).astype(np.int32) >> 17
            b18 = (a & (0b1<<18)).astype(np.int32) >> 18
            b19 = (a & (0b1<<19)).astype(np.int32) >> 19
            b20 = (a & (0b1<<20)).astype(np.int32) >> 20
            b21 = (a & (0b1<<21)).astype(np.int32) >> 21
            b22 = (a & (0b1<<22)).astype(np.int32) >> 22
            b23 = (a & (0b1<<23)).astype(np.int32) >> 23
            b24 = (a & (0b1<<24)).astype(np.int32) >> 24
            b25 = (a & (0b1<<25)).astype(np.int32) >> 25
            b26 = (a & (0b1<<26)).astype(np.int32) >> 26
            b27 = (a & (0b1<<27)).astype(np.int32) >> 27
            b28 = (a & (0b1<<28)).astype(np.int32) >> 28
            b29 = (a & (0b1<<29)).astype(np.int32) >> 29
            b30 = (a & (0b1<<30)).astype(np.int32) >> 30
            b31 = (a & (0b1<<31)).astype(np.int32) >> 31

			#recuperamos los datos juntandolos de nuevo
            a2 = (b31<<31) | (b30<<30) | (b29<<29) | (b28<<28) | (b27<<27) | (b26<<26) | (b25<<25) | (b24<<24) | (b23<<23) | (b22<<22) | (b21<<21) | (b20<<20) | (b19<<19) | (b18<<18) | (b17<<17) | (b16<<16) | (b15<<15) | (b14<<14) | (b13<<13) | (b12<<12) | (b11<<11) | (b10<<10) | (b9<<9) | (b8<<8) | (b7<<7) | (b6<<6) | (b5<<5) | (b4<<4) | (b3<<3) | (b2<<2) | (b1<<1) | (b0<<0)

            a2.astype(np.int32)
            
            # Calculate the inverse transform and store as int16
            # with the numpy library
            array_Out = pywt.waverec(coeffs, 'db1').astype(np.int16)

            stream.write(array_Out.tobytes())
			
			
if __name__ == '__main__':
    main()

stream.stop_stream()
stream.close()

p.terminate()

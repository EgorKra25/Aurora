from curses.ascii import FS
from pickle import FRAME
import pyaudio as pa 
import wave as wv 


def Recorder():
    CHUNK           = 1024
    SAMPLE_FORMAT   = pa.paInt16
    CHANNELS        = 2
    RATE            = 44100
    SECONDS         = 3

    FileNameDict = {
                'SEX'         : "male",
                'AGE'         : "youth",
                'SPEAKER_ID'  : 0,
                'NAME'        : "Egor",
                'NOR'         : 1  # Number of Record
    }

    FileNameDict['SEX']         = input("Your sex: ")
    FileNameDict['AGE']         = input("Your age: ")
    FileNameDict['NAME']        = input("Your name: ")
    FileNameDict['SPEAKER_ID']  = int(input("Your ID: "))

    while True:

        FILENAME = f"{FileNameDict['NAME']}({FileNameDict['SPEAKER_ID']})_{FileNameDict['SEX']}_{FileNameDict['AGE']}_{FileNameDict['NOR']}_output_sound.wav"

        p = pa.PyAudio()
        print("Recording...")

        stream = p.open(
                format=SAMPLE_FORMAT,
                channels=CHANNELS,
                rate=RATE,
                frames_per_buffer=CHUNK,
                input=True
        )

        frames = []

        for _ in range(0, int(RATE / CHUNK*SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close

        p.terminate()

        print("Finish recording!")

        wf = wv.open(FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(SAMPLE_FORMAT))
        wf.setframerate(FS)
        wf.writeframes(b''.join(frames))
        wf.close()

        if('+' == input("do we record again? ")):
            FileNameDict['NOR'] + 1
            continue
        else:
            break
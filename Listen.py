import speech_recognition as sr # pip install speechrecognition
import pyaudio

def listen():

    rec = sr.Recognizer() # call recognizer function from speech_recognition

    with sr.Microphone() as source:  # take input from microphone which is act as source 
                                    # For Microphone module we have to insall pyaudio module "pip install pyaudio"
        print("Listning.....")
        rec.pause_threshold = 1
        audio = rec.listen(source,0,4)  # audio = rec.listen(source,0,2) --> It is recover from continuous listing mode

    try:
        print("Recognizing.....")
        print("    ")
        query = rec.recognize_google(audio,language="en-in")  # Here we use Google recognizer with indian english action 
        print(f"You said : {query}")

    except sr.UnknownValueError:
        print("No speech detected.")
        query = ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        query = ""
        
    query = str(query)
    return query.lower()

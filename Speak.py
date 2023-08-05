import pyttsx3 #pip install pyttsx3

def Say(Text):        # speak is a function which is used for call speak multiple time
    engine = pyttsx3.init("sapi5")      #sapi5 is a speaking engine or software of Microsoft
    voices = engine.getProperty('voices')   #save voices into 'voices' variable
    engine.setProperty('voices',voices[0].id)  #[0] refer to the voice tone
    engine.setProperty('rate',200)  #200 means speed of speaking in pyttsx3 200 = 1x speed
    print("    ")
    print(f"LIMFI : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")
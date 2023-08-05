# Function -> 2 types -. i) Non Innput [ eg : time, Date], ii) Input [ eg: search]

import datetime
from Speak import Say

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputFunc(query):

    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()

    elif "day" in query:
        Day()


def InputFunc(tag,query):

    if "wikipedia" in tag:
        query = str(query).replace("who is","").replace("tell me about","").replace("about","").replace("what is","").replace("when the","").replace("how the","").replace("wikipedia search","")
        import wikipedia
        result = wikipedia.summary(query)
        Say(result)



    elif "google" in tag:
        query = str(query).replace("google","")
        query = (query).replace("search","")
        query = (query).replace("google search","")
        query = (query).replace("search in google","")
        import pywhatkit
        pywhatkit.search(query)


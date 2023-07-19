import random
import json
import torch
import tkinter as tk
from brain import NeuralNetwork
from NeuralNetwork import bag_of_words, tokenize
from Task import NonInputFunc
from Task import InputFunc
from Listen import listen
from Speak import Say

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents and model
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Create the Tkinter GUI window
window = tk.Tk()
window.title("Coco Voice Assistant")
window.geometry("900x600")
window.configure(background="black")

# Create a text widget to display the conversation
conversation_text = tk.Text(window, height=30, width=90, bg="black", fg="white")
conversation_text.pack(pady=20)

# Function to handle user input
def process_input():
    sentence = listen()
    result = str(sentence)

    if sentence == "goodbye":
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probability = torch.softmax(output, dim=1)
    prob = probability[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tags"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputFunc(reply)

                elif "date" in reply:
                    NonInputFunc(reply)

                elif "day" in reply:
                    NonInputFunc(reply)

                elif "wikipedia" in reply:
                    InputFunc(reply, result)

                elif "google" in reply:
                    InputFunc(reply, result)

                else:
                    Say(reply)

                conversation_text.insert(tk.END, "\nYOU : " + result + "\n")
                conversation_text.insert(tk.END, "\nCOCO : " + reply + "\n")
                conversation_text.see(tk.END)

# Create a button for voice input
input_button = tk.Button(window, text="Speak", command=process_input)
input_button.pack()

window.mainloop()

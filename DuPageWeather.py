from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Sean McGovern - Accounting Major self taught Python programmer!')
root.iconbitmap('c:/gui/seanmcgovern.ico')
root.geometry("400x40")
root.configure(background='green')

# URL = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60126&distance=30&API_KEY=079A3D28-93CC-43EA-879A-208778F4DAC8"

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60126&distance=30&API_KEY=079A3D28-93CC-43EA-879A-208778F4DAC8")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except EXCEPTION as e:
    api = "Error..."

myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background="orange")
myLabel.pack()

root.mainloop()
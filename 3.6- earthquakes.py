import urllib.request
import json
from tkinter import *
from tkinter import messagebox

def close_program():
    window.destroy()

def clear_text():
    result_text_widget.config(state="normal")
    result_text_widget.delete(1.0, "end")
    result_text_widget.config(state="disabled")
    
"""def get_screen_dimensions():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    return screen_width, screen_height"""

def print_on_Scrollbar_capo(result_code):
    #Function that shows the text on the scrollbar, on next line
    result_text = str(result_code)
    result_text_widget.config(state="normal")
    result_text_widget.insert("end", "\n" + result_text)
    result_text_widget.config(state="disabled")


def print_on_Scrollbar_nocapo(result_code):
    #Function that shows the text on the scrollbar, on the same line
    result_text = str(result_code)
    result_text_widget.config(state="normal")
    result_text_widget.insert("end", result_text)
    result_text_widget.config(state="disabled")

    
def SearchTool():
    Search = enterTool.get()
    #If "E" starts EarthquakeTool
    if Search == "E":
        urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
        webUrl = urllib.request.urlopen(urlData)
        result_code = "Result code: "
        print_on_Scrollbar_capo(result_code)
        result_code = webUrl.getcode()
        print_on_Scrollbar_nocapo(result_code)
        data = webUrl.read()
        #Call the function
        EarthquakeTool(data)
        
    elif Search == "D":
        urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
        webUrl = urllib.request.urlopen(urlData)
        data = webUrl.read()
        #Call the function
        EarthquakesdepthTool(data)

    elif Search == "L":
        
        #Call the function
        filter_earthquakes_by_location(data)


def EarthquakeTool(data):
    count2 = 0
    count4 = 0
    count6 = 0
    segnato = 0
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        result_code = (theJSON["metadata"]["title"])
        print_on_Scrollbar_capo(result_code)
    count = theJSON["metadata"]["count"]
    result_code = "Events recorded: "
    print_on_Scrollbar_capo(result_code)
    result_code = (count)
    print_on_Scrollbar_nocapo(result_code)
    for i in theJSON["features"]:
        count2 += 1
        result_code = (i["properties"]["place"])
        print_on_Scrollbar_capo(result_code)
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                segnato+=feltReports
                result_code = (i["properties"]["place"], feltReports, "times")
                print_on_Scrollbar_capo(result_code)
    result_code = "TOTAL: "
    print_on_Scrollbar_capo(result_code)
    result_code = count2
    print_on_Scrollbar_nocapo(result_code)
    result_code = "Registered Cases: "
    print_on_Scrollbar_capo(result_code)
    result_code = segnato
    print_on_Scrollbar_nocapo(result_code)

    result_code = "-----------------------------\n"
    print_on_Scrollbar_capo(result_code)
    segnato = 0
    result_code = "Earthquakes with >4.0 magnitude: \n"
    print_on_Scrollbar_capo(result_code)
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            count4 += 1
            result_code = (i["properties"]["place"])
            print_on_Scrollbar_capo(result_code)
            feltReports = i["properties"]["felt"]
            if feltReports != None:
                if feltReports > 0:
                    segnato+=feltReports
                    result_code = (i["properties"]["place"], feltReports, "times")
                    print_on_Scrollbar_capo(result_code)
    result_code = "TOTAL: "
    print_on_Scrollbar_capo(result_code)
    result_code = count4
    print_on_Scrollbar_nocapo(result_code)
    result_code = "Registered Cases: "
    print_on_Scrollbar_capo(result_code)
    result_code = segnato
    print_on_Scrollbar_nocapo(result_code)

    result_code = "-----------------------------\n"
    print_on_Scrollbar_capo(result_code)
    segnato = 0
    result_code = "Earthquakes with >6.0 magnitude: \n"
    print_on_Scrollbar_capo(result_code)
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 6.0:
            count6 += 1
            result_code = (i["properties"]["place"])
            print_on_Scrollbar_capo(result_code)
            feltReports = i["properties"]["felt"]
            if feltReports != None:
                if feltReports > 0:
                    result_code = (i["properties"]["place"], feltReports, "times")
                    print_on_Scrollbar_capo(result_code)
    result_code = "TOTAL: "
    print_on_Scrollbar_capo(result_code)
    result_code = count6
    print_on_Scrollbar_nocapo(result_code)
    result_code = "Registered Cases: "
    print_on_Scrollbar_capo(result_code)
    result_code = segnato
    print_on_Scrollbar_nocapo(result_code) 
    pass


def EarthquakesdepthTool(data):
    theJSON = json.loads(data)
    result_code = "Depth of each Earthquakes:"
    print_on_Scrollbar_capo(result_code)
    for i in theJSON["features"]:
        depth = i["geometry"]["coordinates"][2]  # Profondità
        result_code = depth
        print_on_Scrollbar_capo(result_code)


def filter_earthquakes_by_location():
    search_location = enterTool.get().lower()  # Converti il testo inserito in minuscolo per la corrispondenza case-insensitive
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    data = webUrl.read()
    theJSON = json.loads(data)
    result_text_widget.config(state="normal")
    result_text_widget.delete(1.0, "end")

    for earthquake in theJSON["features"]:
        location = earthquake["properties"]["place"].lower()

        # Confronta il luogo del terremoto con il luogo inserito dall'utente
        if search_location in location:
            result_text_widget.insert("end", f"Place: {location}\n")
            result_text_widget.insert("end", f"Magnitude: {earthquake['properties']['mag']}\n")
            result_text_widget.insert("end", f"Time: {earthquake['properties']['time']}\n")
            result_text_widget.insert("end", "\n")

    result_text_widget.config(state="disabled")


#----------------------------------------------------------------------------
#GRAPHIC:
window = Tk()
window.title("Tools")
#screen_width, screen_height = get_screen_dimensions()
window.geometry("640x480")
window.configure(bg="Black")
lab1 = Label(window, text="Please select the tool", font=("Serif",16, "bold"), bg="Black", fg="White")
lab1.place (x=0, y=18)
enterTool = Entry(window)
enterTool.place (x=0, y=50)
insertBtn = Button(window, text="Search", font=("Sans", 12), bg="Black", fg="White", command=SearchTool)
insertBtn.place (x=170, y=45)
insertLocBtn = Button(window, text="Search Location", font=("Sans", 12), bg="Black", fg="White", command=filter_earthquakes_by_location)
insertLocBtn.place (x=250, y=45)

#Label that shows results:
result_text_widget = Text(window, font=("Sans", 12), height=20, width=63, bg="Black", fg="White")
result_text_widget.place(x=0, y=80)

scrollbar = Scrollbar(window, command=result_text_widget.yview)
scrollbar.place(x=620, y=80, relheight=0.8)
result_text_widget.config(yscrollcommand=scrollbar.set)

#Button to clear the scrollbar
clearBtn = Button(window, text="Clear board", font=("Sans", 12), bg="Black", fg="White", command=clear_text)
clearBtn.place(x=410, y=20)

#Button to close the program
closeBtn = Button(window, text="Quit", font=("Sans", 12), bg="Black", fg="White", command=close_program)
closeBtn.place(x=550, y=20)

'''
READ ME:

Functions: haversine, longlat, fly_dist, to_tuple, reader, parsFormDictEntry
Class: FlyingDist; class methods: define_widgets, displayDepCity, displayDestCity, calculate, readerMethod

---

### DESCRIPTION(haversine):
`haversine` is a function that calculates the great-circle distance between two points on a sphere given their longitudes and latitudes in radians.

#### PARAMETERS:
- `latrad1` (float): Latitude of the first point in radians.
- `lonrad1` (float): Longitude of the first point in radians.
- `latrad2` (float): Latitude of the second point in radians.
- `lonrad2` (float): Longitude of the second point in radians.

#### LIMITATIONS(haversine):
- Assumes inputs are in radians, thus requiring conversion if in degrees.
- Ignores elevation differences, affecting accuracy for specific use cases.

#### STRUCTURES(haversine):
- The function uses multiple mathematical operations to compute the distance using the haversine formula.

#### OUTPUT(haversine):
- Returns the distance in radians between two points on a sphere.

---

### DESCRIPTION(longlat):
`longlat` converts geographic coordinates from degrees, minutes, and direction (N/S/E/W) to radians.

#### PARAMETERS:
- `inp1` (float): Degrees of latitude or longitude.
- `inp2` (float): Minutes of latitude or longitude.
- `inp3` (str): Direction (N, S, E, W).

#### LIMITATIONS(longlat):
- The function raises an exception for invalid direction inputs.
- It does not handle incorrect or malformed input types beyond basic validation.

#### STRUCTURES(longlat):
- Uses if-elif-else to determine the sign of the coordinate based on direction.

#### OUTPUT(longlat):
- Returns the geographic coordinate in radians.

---

### DESCRIPTION(fly_dist):
`fly_dist` calculates the flying distance between two sets of coordinates, from degrees and minutes to distance in kilometers.

#### PARAMETERS:
- `set1` (tuple): The first set of coordinates.
- `set2` (tuple): The second set of coordinates.

#### LIMITATIONS(fly_dist):
- Assumes valid input format as tuples; malformed inputs can cause errors.
- Computationally intensive for large datasets or repeated calls.

#### STRUCTURES(fly_dist):
- Uses nested function calls and mathematical operations to convert coordinates and calculate distance.

#### OUTPUT(fly_dist):
- Returns the distance in kilometers between two points.

---

### DESCRIPTION(to_tuple):
`to_tuple` converts a line from a file with city and coordinates information into a structured tuple.

#### PARAMETERS:
- `a_line` (str): A line from the file containing city and coordinates information.

#### LIMITATIONS(to_tuple):
- Assumes a specific format for the input string, leading to potential errors with unexpected formats.
- Limited error handling; invalid inputs might cause the function to fail.

#### STRUCTURES(to_tuple):
- Uses regex to parse the line and extract relevant information.

#### OUTPUT(to_tuple):
- Returns a tuple containing city name and coordinates.

---

### DESCRIPTION(reader):
`reader` reads a file and returns a dictionary with city information.

#### PARAMETERS:
- `filename` (str): The name of the file containing city data.

#### LIMITATIONS(reader):
- Assumes the file is well-formed and accessible; lacks robust error handling for file I/O.
- Performance issues with very large files due to memory constraints.

#### STRUCTURES(reader):
- Uses a loop to read each line of the file and convert it to a tuple using `to_tuple`.

#### OUTPUT(reader):
- Returns a dictionary with city names as keys and tuples with city data as values.

---

### DESCRIPTION(parsFormDictEntry):
`parsFormDictEntry` formats a dictionary entry of a city into a readable string format.

#### PARAMETERS:
- `dictEntry` (tuple): A dictionary entry containing city name and coordinates.

#### LIMITATIONS(parsFormDictEntry):
- Assumes input is correctly formatted as per the expected dictionary entry structure.
- Limited to the specific dictionary format used in this program.

#### STRUCTURES(parsFormDictEntry):
- Uses string formatting to create a readable string from the input tuple.

#### OUTPUT(parsFormDictEntry):
- Returns a formatted string representation of the dictionary entry.

---

### DESCRIPTION(FlyingDist):
`FlyingDist` is a class that creates a GUI to calculate and display the flying distance between two cities selected from a list.

#### DESCRIPTION(__init__):
Initializes the GUI, setting up necessary variables and calling `define_widgets`.

#### DESCRIPTION(define_widgets):
Sets up and configures the GUI components, including labels, listboxes, buttons, and entry widgets.

#### DESCRIPTION(displayDepCity):
Displays the selected departure city and its coordinates when selected from the listbox.

#### DESCRIPTION(displayDestCity):
Displays the selected destination city and its coordinates when selected from the listbox.

#### DESCRIPTION(calculate):
Calculates the flying distance between the selected departure and destination cities and updates the GUI.

#### DESCRIPTION(readerMethod):
Reads a file containing city data and updates the current dictionary with new cities.

#### PARAMETERS(FlyingDist):
n/a

#### LIMITATIONS(FlyingDist Class):
- Dependent on `tkinter`, which may not be suitable for all environments.
- Limited to predefined city data unless updated via file input.

#### LIMITATIONS(define_widgets):
- Fixed layout that does not adapt to window resizing.
- Limited customization options for widget positions and sizes.

#### LIMITATIONS(displayDepCity):
- Assumes valid selection from the listbox; lacks robust error handling.
- Limited to displaying information of preloaded or read-in cities.

#### LIMITATIONS(displayDestCity):
- Same as `displayDepCity`.

#### LIMITATIONS(calculate):
- Assumes valid city selections; errors can occur if no city is selected.
- Performance issues with large datasets due to repeated calculations.

#### LIMITATIONS(readerMethod):
- Assumes the file is well-formed; errors can occur with malformed files.
- Reinitializes the entire GUI upon reading new data, potentially causing performance issues.

#### STRUCTURES(define_widgets):
- Uses loops to populate listboxes and bind events to widget actions.

#### STRUCTURES(displayDepCity):
- Uses an if-statement to check for a valid selection and update display variables.

#### STRUCTURES(displayDestCity):
- Same as `displayDepCity`.

#### STRUCTURES(calculate):
- Sequentially retrieves city data and calculates the distance using nested function calls.

#### STRUCTURES(readerMethod):
- Uses a loop to read and update the dictionary with new city data, reinitializing the GUI.

#### OUTPUT(define_widgets):
- Configures and displays GUI components without direct output.

#### OUTPUT(displayDepCity):
- Updates display variables with selected city information.

#### OUTPUT(displayDestCity):
- Same as `displayDepCity`.

#### OUTPUT(calculate):
- Sets the calculated distance in the output variable, updating the GUI display.

#### OUTPUT(readerMethod):
- Prints the updated city dictionary to the console and updates the GUI components.
'''


import math
import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#Set of three calculation functions
#calculation function distance in radians
def haversine(latrad1, lonrad1, latrad2, lonrad2):
    g = (math.sin((latrad2 - latrad1) / 2)) ** 2
    h = math.cos(latrad1) * math.cos(latrad2)
    k = (math.sin((lonrad2 - lonrad1) / 2)) ** 2
    a_squared = g + h * (k)
    b_squared = 1 - a_squared
    a = a_squared ** .5
    b = b_squared ** .5
    d = 2 * math.atan2(a, b)
    return d

#calculation function from degrees, minutes and sign to radians
def longlat(inp1, inp2, inp3):
    inp1 = float(inp1)
    inp2 = float(inp2)
    if inp3 == 'E' or inp3 == 'N' or inp3 == 'e' or inp3 == 'n':
        l = 1
    elif inp3 == 'W' or inp3 == 'S' or inp3 == 'w' or inp3 == 's':
        l = -1
    else:
        raise Exception('The latitude or longitude letter (N,E,S,W) was not given correctly')
    inp = l * (inp1 + inp2 / 60)
    outrad = (inp / 360) * 2 * math.pi
    return outrad

#calculation function from coordinates, to radians, to distance in radians, to distance in km
def fly_dist(set1, set2):
    latrad1 = longlat(set1[1][0], set1[1][1], set1[1][2])
    latrad2 = longlat(set2[1][0], set2[1][1], set2[1][2])
    lonrad1 = longlat(set1[2][0], set1[2][1], set1[2][2])
    lonrad2 = longlat(set2[2][0], set2[2][1], set2[2][2])
    distrad = haversine(latrad1, lonrad1, latrad2, lonrad2)
    dist = 40005 * distrad / (2 * math.pi)
    return dist


#Set of two functions, from file to a dictionary containing the cities with their information
#function that takes a line from a file with a city with coordinates
# and returns a tuple in the correct format for the dictionary
def to_tuple(a_line):
    pattern = r'(.*),\s(.*?)\s(\d+)\s(\d+)\s([NSns])\s(\d+)\s(\d+)\s([WEwe])'

    matcher = re.compile(pattern)
    match = matcher.search(a_line)
    if match != None:
        name = match.group(1)
        lat_deg = match.group(3)
        lat_min = match.group(4)
        lat_sign = match.group(5)
        lon_deg = match.group(6)
        lon_min = match.group(7)
        lon_sign = match.group(8)
    lat_deg = int(lat_deg)
    lat_min = int(lat_min)
    lon_deg = int(lon_deg)
    lon_min = int(lon_min)

    lat = lat_deg, lat_min, lat_sign
    lon = lon_deg, lon_min, lon_sign
    result = name, lat, lon
    return result

#function that takes a file and a dictionary
# and returns the cities from the file included in that dictionary
def reader(filename):
    cities = {}
    f = open(filename, 'r')
    for line in f:
        city = to_tuple(line)
        name, lat, lon = city
        cities[name] = city
    f.close()
    return cities

#standard dictionary
city_dict = {'Amsterdam': ('Amsterdam', (52, 22, 'N'), (4, 32, 'E')),
             'Montreal': ('Montreal', (45, 30, 'N'), (73, 35, 'W')),
             'Auckland': ('Auckland', (36, 52, 'S'), (174, 45, 'E'))}

def parsFormDictEntry(dictEntry):
    (name, (lat_deg, lat_min, lat_sign), (lon_deg, lon_min, lon_sign)) = dictEntry
    format = "%d%s%d'%s %d%s%d'%s"
    string = format % (lat_deg, chr(176), lat_min, lat_sign, lon_deg, chr(176), lon_min, lon_sign)
    return string


import tkinter as tk

class FlyingDist(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('Flying distances GUI')
        self.destination = tk.Entry(self)
        self.depSelect_city = tk.StringVar()
        self.destSelect_city = tk.StringVar()
        self.depSelectCoord = tk.StringVar()
        self.destSelectCoord = tk.StringVar()
        self.outputDist = tk.IntVar()
        self.fileName = tk.StringVar()
        self.currentDict = city_dict
        self.define_widgets()
        self.grid()

    def define_widgets(self):

        # label for departure city
        lbl_city = tk.Label(self)
        lbl_city['text'] = "Departure city"
        lbl_city.grid(row=0, column=0)

        # entry box for city names
        self.departure_city = tk.Listbox(self, selectmode=tk.SINGLE)
        self.departure_city.grid(row=1, column=0, rowspan=10)
        for city in self.currentDict.keys():
            self.departure_city.insert(tk.END, city)
        self.departure_city.bind("<<ListboxSelect>>", self.displayDepCity)

        # label for filename
        lbl_filename = tk.Label(self)
        lbl_filename['text'] = "Filename:"
        lbl_filename.grid(row=11, column=0, sticky='E')

        # The center two columns
        btn_cal = tk.Button(self)
        btn_cal['text'] = 'Calculate'
        btn_cal['command'] = self.calculate
        btn_cal.grid(row=1, column=1, columnspan = 2)

        lbl_depCity = tk.Label(self)
        lbl_depCity['text'] = 'Dep. city:'
        lbl_depCity.grid(row=2, column=1)

        lbl_destCity = tk.Label(self)
        lbl_destCity['text'] = 'Dest. city:'
        lbl_destCity.grid(row=2, column=2)

        lbl_depCityName = tk.Label(self)
        lbl_depCityName['textvariable'] = self.depSelect_city
        lbl_depCityName.grid(row=3, column=1)

        lbl_destCityName = tk.Label(self)
        lbl_destCityName['textvariable'] = self.destSelect_city
        lbl_destCityName.grid(row=3, column=2)

        lbl_depCoord = tk.Label(self)
        lbl_depCoord['text'] = 'Dep. city coord:'
        lbl_depCoord.grid(row=4, column=1)

        lbl_destCoord = tk.Label(self)
        lbl_destCoord['text'] = 'Dest. city coord:'
        lbl_destCoord.grid(row=4, column=2)

        lbl_depCityCoord = tk.Label(self)
        lbl_depCityCoord['textvariable'] = self.depSelectCoord
        lbl_depCityCoord.grid(row=5, column=1)

        lbl_destCityCoord = tk.Label(self)
        lbl_destCityCoord['textvariable'] = self.destSelectCoord
        lbl_destCityCoord.grid(row=5, column=2)

        lbl_title = tk.Label(self)
        lbl_title['text'] = 'Flying distance:'
        lbl_title.grid(row=6, column=1, columnspan = 2)

        lbl_outputDist = tk.Label(self)
        lbl_outputDist['textvariable'] = self.outputDist
        lbl_outputDist.grid(row=7, column=1, columnspan = 2)

        ent_file = tk.Entry(self)
        ent_file['textvariable'] = self.fileName
        ent_file.grid(row=11, column=1, columnspan = 2, sticky='W')


        # The right column

        lbl_destination = tk.Label(self)
        lbl_destination['text'] = 'Destination city'
        lbl_destination.grid(row=0, column=3)

        self.destination_city = tk.Listbox(self, selectmode=tk.SINGLE)
        self.destination_city.grid(row=1, column=3, rowspan=10)
        for city in self.currentDict.keys():
            self.destination_city.insert(tk.END, city)
        self.destination_city.bind("<<ListboxSelect>>", self.displayDestCity)

        btn_read = tk.Button(self)
        btn_read['text'] = 'Read in'
        btn_read['command'] = self.readerMethod
        btn_read.grid(row=11, column=3, sticky='W')

    def displayDepCity(self, event):
        selectDep = self.departure_city.curselection()
        if selectDep:
            self.depSelect_city.set(self.departure_city.get(selectDep))
            set1 = self.currentDict[my_gui.depSelect_city.get()]
            self.depSelectCoord.set(parsFormDictEntry(set1))

    def displayDestCity(self, event):
        selectDest = self.destination_city.curselection()
        if selectDest:
            self.destSelect_city.set(self.destination_city.get(selectDest))
            set2 = self.currentDict[my_gui.destSelect_city.get()]
            self.destSelectCoord.set(parsFormDictEntry(set2))

    def calculate(self):
        set1 = self.currentDict[my_gui.depSelect_city.get()]
        set2 = self.currentDict[my_gui.destSelect_city.get()]
        self.outputDist.set(int(fly_dist(set1, set2)))

    def readerMethod(self):
        addCityDict = reader(str(self.fileName.get()))
        self.currentDict.update(addCityDict)
        tempNames = list(self.currentDict.keys())
        tempNames.sort()
        tempDict = {}
        for key in tempNames:
            tempDict[key] = self.currentDict[key]
        self.currentDict = tempDict.copy()
        self.define_widgets()


my_gui = FlyingDist()
my_gui.mainloop()


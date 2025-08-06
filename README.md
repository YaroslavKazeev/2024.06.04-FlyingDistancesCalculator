# Flying Distances Calculator

A Python GUI application that calculates the great-circle distance between two cities using their geographic coordinates. The application provides an interactive interface for selecting departure and destination cities and displays the calculated flying distance in kilometers.

## Features

- **Interactive GUI**: User-friendly interface built with Tkinter
- **City Selection**: Dropdown lists for selecting departure and destination cities
- **Coordinate Display**: Shows geographic coordinates for selected cities
- **Distance Calculation**: Calculates great-circle distance using the Haversine formula
- **File Import**: Ability to load additional city data from text files
- **Real-time Updates**: Dynamic display of city information and calculated distances

## Mathematical Background

The application uses the **Haversine formula** to calculate the great-circle distance between two points on Earth's surface:

```
a = sin²(Δφ/2) + cos(φ₁) × cos(φ₂) × sin²(Δλ/2)
c = 2 × atan2(√a, √(1−a))
d = R × c
```

Where:

- φ₁, φ₂ are the latitudes of the two points
- λ₁, λ₂ are the longitudes of the two points
- R is Earth's radius (approximately 6,371 km)

import csv
import pyproj

def utm_to_latlong(zone, easting, northing, northern=True):
    """Convert UTM coordinates to latitude and longitude.
    Returns a tuple of (latitude, longitude).
    """
    if not northern:
        northing = 10000000 - northing

    proj_string = f"+proj=utm +zone={zone} +ellps=WGS84 +datum=WGS84 +units=m +no_defs"
    p = pyproj.Proj(proj_string)
    return p(easting, northing, inverse=True)

# Read the input CSV file
with open("input.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Convert the UTM coordinates to latitude and longitude
for row in data:
    zone = int(row["Zone"])
    easting = float(row["Easting"])
    northing = float(row["Northing"])
    latitude, longitude = utm_to_latlong(zone, easting, northing)
    row["Latitude"] = latitude
    row["Longitude"] = longitude

# Write the output CSV file
fieldnames = ["Zone", "Easting", "Northing", "Latitude", "Longitude"]
with open("output.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

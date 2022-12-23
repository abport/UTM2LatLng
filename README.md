# Batch Convert UTM to Latitude and Longitude
Batch Convert UTM coordinates to latitude and longitude using Python

The script uses the pyproj library to convert UTM coordinates to latitude and longitude. You will need to install this library in order to run the script, by running the following command:

```python
pip install pyproj
```

**Introduction**

UTM (Universal Transverse Mercator) coordinates are a standard way of specifying positions on the surface of the Earth. They are commonly used in maps and geographic information systems (GIS). However, many applications require coordinates to be specified in latitude and longitude, rather than UTM. In this blog post, we will look at how to convert UTM coordinates to latitude and longitude using Python.

**Converting UTM to Latitude and Longitude**

To convert UTM coordinates to latitude and longitude, we will use the pyproj library. This library provides functions for converting between different map projections.

First, let's define a function `utm_to_latlong()` that takes UTM zone, easting, and northing coordinates as arguments, and returns a tuple of (latitude, longitude). The function also takes an optional argument `northern`, which indicates whether the coordinates are in the northern or southern hemisphere. If `northern` is False, we subtract the northing coordinate from 10 million, since UTM coordinates use a different northing origin in the southern hemisphere.

```python
def utm_to_latlong(zone, easting, northing, northern=True):
    """Convert UTM coordinates to latitude and longitude.
    Returns a tuple of (latitude, longitude).
    """
    if not northern:
        northing = 10000000 - northing
```
Next, we create a projection object using the UTM zone and the WGS84 ellipsoid. This projection object will be used to convert between UTM and latitude/longitude coordinates.

```python
    proj_string = f"+proj=utm +zone={zone} +ellps=WGS84 +datum=WGS84 +units=m +no_defs"
    p = pyproj.Proj(proj_string)
```
Finally, we use the projection object's `p()` method to convert the UTM coordinates to latitude and longitude. The `inverse` parameter is set to `True` to indicate that we are performing an inverse transformation (i.e., from UTM to latitude/longitude).

```python
    return p(easting, northing, inverse=True)
```
**Batch Conversion**

Now that we have a function to convert UTM coordinates to latitude and longitude, we can use it to batch convert a large number of coordinates. To do this, we will read a CSV file containing the UTM coordinates, and write the resulting latitude and longitude values to a new CSV file.

We will use the Python `csv` module to read and write the CSV files. First, we open the input CSV file and read it into a list of dictionaries using the `csv.DictReader()` function.

```python
with open("input.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
```
The input CSV file should have the following format:

```
Zone,Easting,Northing
31,444238,4447647
32,234562,5466987
...
```
Next, we iterate through the list of dictionaries, and use the `utm_to_latlong()` function to convert the UTM coordinates to latitude and longitude. We then add the latitude and longitude values to the dictionary for each row.
```python
for row in data:
    zone = int(row["Zone"])
    easting = float(row["Easting"])
    northing = float(row["Northing"])
    latitude, longitude = utm_to_latlong(zone, easting, northing)
    row["Latitude"] = latitude
    row["Longitude"] = longitude
```
in the loop above, we convert the UTM coordinates for each row to latitude and longitude using the `utm_to_latlong()` function, and add the resulting values to the dictionary for each row.

Finally, we open the output CSV file and write the modified data to it using the `csv.DictWriter()` function.

```python
with open("output.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

The output CSV file will have the same format as the input file, with the addition of two new columns, "Latitude" and "Longitude", containing the converted coordinates.

**Conclusion**

In this blog post, we saw how to convert UTM coordinates to latitude and longitude using the pyproj library in Python. We also looked at how to batch convert a large number of coordinates from a CSV file, and write the resulting coordinates to a new CSV file. This technique can be useful in a variety of GIS and mapping applications.

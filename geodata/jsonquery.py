import json

input_file = 'Amtrak_Routes.geojson'
output_file = 'NortheastRegional.json'
route = ['29']

# Load GeoJSON
with open(input_file, 'r') as file:
    data = json.load(file)

# Filter features
filtered_features = [feature for feature in data['features'] 
                     if feature['properties']['objectid'] in route]

# Create new GeoJSON
new_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

# Save to file
with open(output_file, 'w') as file:
    json.dump(new_geojson, file)
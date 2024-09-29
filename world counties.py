
import folium
import csv

geoJsonFileName = "C:/Users/shunt/nasa/COUNTIES_POLYM.json"



nyCenter =        (40.7128, -74.0060)
nyCountyCenters = {
    }
maCountyCenters = {
    }
foreignCenters = {
    "Toronto": (43.6532, -79.3832),
    "Gothemburg": (57.7089, 11.9746),
    "Copenhagen": (55.6761, 12.5683),
    "Tokyo": (35.6764, 139.6500)
    }

with open("uscounties.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        if row[5] == "New York":
            nyCountyCenters[row[1]] = (row[6],row[7])
            continue
        if row[5] == "Massachusetts":
            maCountyCenters[row[1]] = (row[6],row[7])
            continue

usMap = folium.Map(location = nyCenter, zoom_start = 8)

nyCountiesLayer = folium.GeoJson(
    "ny-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

nhCountiesLayer = folium.GeoJson(
    "nh-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

flCountiesLayer = folium.GeoJson(
    "fl-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

paCountiesLayer = folium.GeoJson(
    "pa-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

ctCountiesLayer = folium.GeoJson(
    "ct-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

riCountiesLayer = folium.GeoJson(
    "ri-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

njCountiesLayer = folium.GeoJson(
    "nj-counties.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

maCenter =        (42.4072, -71.3824)


folium.GeoJson(
    geoJsonFileName,
    style_function = lambda geoJsonFeatures: {
        "color": "darkblue",
        "weight": 2,
        "fillColor": "lightblue"
            if geoJsonFeatures["properties"]["COUNTY"] == "Middlesex"
            else "transparent",
        "fillOpacity": 0,
    },
).add_to(usMap)

shunSoccerLocations = {
    "Suny Purchase Turf Field":    ( 41.043512, -73.696910),
    "Ophir Field ":    ( 41.033314, -73.718289),
    "New Utrecht High School ":    ( 40.612742, -74.001801),
    "Capelli Sports Complex":    (40.275686, -74.083336 ),
    "Mater Salvatoris College Preparatory School":    ( 41.092598, -73.535970),
    "FDU Soccer Field":    ( 40.902800, -74.026506),
    "Woburn Football Field":    (42.483316, -71.145654 ),
    "Nugent Stadium":    (40.973214, -73.689380),
    "West Street Park":    (40.983049, -73.736015),
    "Tappan Zee High School ":    (41.049092, -73.951342),
    "Glover Field":    (40.898533, -73.817128),
    "Blandford Field":    (41.001555, -73.811959),
    "Spring Valley High School":    (41.105296, -74.055093),
    "New Rochelle High School":    (40.930253, -73.792959),
    "The Ursuline School":    (40.950242, -73.796886),
    "Flowers Park":    (40.930266, -73.773734),
    "Lakeland High School":    (41.324191, -73.837881),
    "Eastchester High School":    (40.960159, -73.808998),
    "Fayetteville-Manlius High School": (43.008229, -75.962041),
    "Tuckahoe Turf Farms Soccer Fields": (39.687002, -74.794691)
    
    }

shunBaseballLocations = {
    "Lyon Park":    (41.014038, -73.664014),
    "Disbrow Park":    (40.964566, -73.688973),
    "Gagliardo Park":    (40.980599, -73.695161),
    "Brentwood Baseball Field":    (40.971506, -73.722081),
    "Walter Panas High School":    (41.280251, -73.861934),
    "Doubleday Field":    (42.699063, -74.927133),
    "White Plains High School":    (41.018864, -73.735660)
    
    }
hannaTennisLocations = {
    "Bedford High School":    (42.49000423825486, -71.28466682478394),
    "Longfellow New Hampshire Tennis Club":    (42.768991595716436, -71.45233125841023),
    "Longfellow Wayland Tennis Club":    (42.365566276455354, -71.38844644493363),
    "Longfellow Natick Tennis Club":    (42.31445771046814, -71.33694551794996),
    "Woburn Racquet Club":    (42.51062740373581, -71.16690563191075),
    "Meadowbrook Country Club":    (42.560221614887205, -71.12426080603286),
    "Tufts University Steve Tisch Sports and Fitness Center":    (42.409048172677565, -71.11553154723677),
    "Winchester Indoor Tennis Club":    (42.469746063761946, -71.13702463065587),
    "Medford Playstead Tennis Courts":    (42.42608682761812, -71.13725982621794),
    "Sagamihara Fuchinobe Park":    (35.55610849766407, 139.39284778177202)
    
    }
reiSoccerLocations = {
    "New England Futbol Club Field":    (42.09755, -71.50334),
    "Massachusetts Youth Soccer Fields":    (42.516843, -71.695477),
    "Providence Country Day School Field":    (41.816115, -71.354261),
    "Toronto FC Field":    (43.443760, -71.282410),
    "NYCFC":    (40.432710, -73.473500),
    "New England Revolution Field":    (42.050730, -71.160200),
    "Met Oval Field":    (40.425300, -73.542700),
    "Seacoast Field":    (42.305920, -71.414340),
    "Oakwood Field":    (41.361860, -72.360570),
    "NEFC Field":    (42.055100, -71.301360),
    "FC Valeo Field":    (42.172490, -71.114150),
    "Boston Bolts":    (42.174220, -71.114210),
    "Gottschee":    (40.431070, -73.530380)
    }


allLocations = hannaTennisLocations | shunSoccerLocations | shunBaseballLocations | reiSoccerLocations

for locationName, latLon in allLocations.items():
    folium.Marker(
        latLon,
        popup = folium.Popup(
            f"<b>{locationName}</b><p>some extra info</p>"),
        icon = folium.Icon(color="red", icon="ball")
    ).add_to(usMap)

for countyName, countyCenter in nyCountyCenters.items():
    folium.Marker(
        countyCenter,
        popup = folium.Popup(
            f"<b>{countyName}</b><p>some extra info</p>"),
    ).add_to(usMap)
    
for countyName, countyCenter in maCountyCenters.items():
    folium.Marker(
        countyCenter,
        popup = folium.Popup(
            f"<b>{countyName}</b><p>some extra info</p>"),
    ).add_to(usMap)
    
for countyName, countyCenter in foreignCenters.items():
    folium.Marker(
        countyCenter,
        popup = folium.Popup(
            f"<b>{countyName}</b><p>some extra info</p>"),
    ).add_to(usMap)
    


usMap.save("us-counties-markers.html")





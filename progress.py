
import folium

nyCenter =        (40.7128, -74.0060)
nyCountyCenters = {
    "Kings": (40.6413, -73.9383),
    "Queens":  (40.7035, -73.8196),
    "New York":    (40.7792, -73.9668),
    "Suffolk":      (40.8681, -72.8456),
    "Bronx":      (40.8501, -73.8672),
    "Nassau":   (40.7326, -73.5862),
    "Westchester":    (41.1626, -73.7561),
    "Erie":  (42.7639, -78.7323),
    "Monroe":  (43.1464, -77.6961),
    "Richmond":  (40.5808, -74.1531),
    "Onondaga":   (43.0058, -76.1946),
    "Orange":    (41.4022, -74.3056),
    "Rockland":  (41.1525, -74.0242),
    "Albany":    (42.6002, -73.9736),
    "Dutchess":    (41.7652, -73.7429),
    "Saratoga":    (43.1074, -73.8639),
    "Oneida":    (43.2418, -75.4358),
    "Niagara":    (43.2001, -78.7452),
    "Broome":    (42.1602, -75.8196),
    "Ulster":    (41.8881, -74.2586),
    "Rensselaer":    (42.7111, -73.5097),
    "Schenectady":    (42.8181, -74.0586),
    "Chautauqua":    (42.2281, -79.3663),
    "Oswego":    (43.4269, -76.1413),
    "Jefferson":    (44.0496, -75.9203),
    "Ontario":    (42.8528, -77.2998),
    "St. Lawrence":    (44.4964, -75.0691),
    "Tompkins":    (42.452, -76.4736),
    "Putnam":    (41.4267, -73.7495),
    "Steuben":    (42.2678, -77.3838),
    "Wayne":    (43.1566, -77.0294),
    "Chemung":    (42.1413, -76.76),
    "Clinton":    (44.7462, -73.6782),
    "Sullivan":    (41.7164, -74.7681),
    "Cattaraugus":    (42.2486, -78.6788),
    "Cayuga":    (42.9175, -76.5545),
    "Madison":    (42.9128, -75.6696),
    "Warren":    (43.561, -73.846),
    "Livingston":    (42.728, -77.7755),
    "Columbia":    (42.2501, -73.6318),
    "Washington":    (43.3137, -73.4308),
    "Herkimer":    (43.4193, -74.9624),
    "Otsego":    (42.6338, -75.0326),
    "Genesee":    (43.0009, -78.1937),
    "Fulton":    (43.1138, -74.4222),
    "Montgomery":    (42.9023, -74.4397),
    "Tioga":    (42.1703, -76.3063),
    "Greene":    (42.2765, -74.1227),
    "Franklin":    (44.5929, -74.3038),
    "Allegany":    (42.2574, -78.0276),
    "Chenango":    (42.4935, -75.6116),
    "Cortland":    (42.595, -76.0703),
    "Delaware":    (42.1981, -74.9665),
    "Wyoming":    (42.7024, -78.2244),
    "Orleans":    (43.2521, -78.2312),
    "Essex":    (44.1172, -73.7726),
    "Seneca":    (42.7811, -76.8238),
    "Schoharie":    (42.5882, -74.4421),
    "Lewis":    (43.7851, -75.4486),
    "Yates":    (42.6335, -77.1055),
    "Schuyler":    (42.3938, -76.8752),
    "Hamilton":    (43.6611, -74.4974),

    }

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
    "Fayetteville-Manlius High School": (43.008229, -75.962041)
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
    
    }

usMap = folium.Map(location = nyCenter, zoom_start = 8)

usCountiesLayer = folium.GeoJson(
    "us-states.json",
    style_function=lambda feature: {
        "color": "darkblue",
        "weight": 2,
        "fillOpacity": 0,
    },
).add_to(usMap)

for countyName, countyCenter in nyCountyCenters.items():
    folium.Marker(
        countyCenter,
        popup = folium.Popup(
            f"<b>{countyName}</b><p>some extra info</p>"),
    ).add_to(usMap)
    
for fieldname, field in shunSoccerLocations.items():
    folium.Marker(
        field,
        popup = folium.Popup(
            f"<b>{fieldname}</b><p>some extra info</p>"),
        icon = folium.Icon(color="black", icon="ball")
    ).add_to(usMap)
    
for fieldname, field in shunBaseballLocations.items():
    folium.Marker(
        field,
        popup = folium.Popup(
            f"<b>{fieldname}</b><p>some extra info</p>"),
        icon = folium.Icon(color="red", icon="ball")
    ).add_to(usMap)
    
for courtname, court in hannaTennisLocations.items():
    folium.Marker(
        court,
        popup = folium.Popup(
            f"<b>{courtname}</b><p>some extra info</p>"),
        icon = folium.Icon(color="green", icon="ball")
    ).add_to(usMap)
    


usMap.save("us-counties-markers.html")






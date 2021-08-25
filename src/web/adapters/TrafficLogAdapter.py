

def traffic_log_adapter(item):

    vehicle_id = int(item['car'])
    date = item['date']
    location = item['location']

    split_to_Brace = location.split('(')
    split_to_Space = split_to_Brace[1].split(' ')
    latitude = float(split_to_Space[0])
    split_from_right = split_to_Space[1].split(')')
    longitude = float(split_from_right[0])
    return {"vehicle_id": vehicle_id, "date": date, "latitude": latitude, "longitude": longitude,
            "road_id": None, "vehicle_type": None, "vehicle_color": None, "road_width": None, "province_name": None}





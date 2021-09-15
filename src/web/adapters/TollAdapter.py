from src.domain.models.DriverDomainModel import DriverDomainModel
import datetime


def toll_adapter(item):
    light_vehicle_charge = item.get('toll_per_cross')
    location = item['location']
    split_to_Brace = location.split('(')
    split_to_Space = split_to_Brace[1].split(' ')
    latitude = float(split_to_Space[0])
    split_from_right = split_to_Space[1].split(')')
    longitude = float(split_from_right[0])
    return {'road_id': None, 'name': item.get("name"), 'light_vehicle_charge': light_vehicle_charge,
            'heavy_vehicle_charge': None, 'heavy_vehicle_charge_per_kg': None, 'latitude': latitude, 'longitude': longitude}

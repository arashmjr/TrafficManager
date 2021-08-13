from src.domain.models.TollDomainModel import TollDomainModel
from src.repository.TollRepository import TollRepository
from src.repository.TrafficLogRepository import TrafficLogRepository
from src.domain.models.TrafficLogDomainModel import TrafficLogDomainModel
from django.utils import timezone
import haversine as hs


class TrafficLogService:
    repository_log: TrafficLogRepository
    repository_station: TollRepository

    def __init__(self, repository_log: TrafficLogRepository, repository_station: TollRepository):
        self.repository_log = repository_log
        self.repository_station = repository_station

    def add_traffic_log(self, json):

        date = timezone.now()
        model = TrafficLogDomainModel(json['road_id'], json['vehicle_id'], json['vehicle_type'],
                                      json['vehicle_color'], json['road_width'], date,
                                      json['province_name'], json['latitude'], json['longitude'])

        self.repository_log.insert(model)
        return True

    def get_logs_by(self, max_road_width: int, vehicle_type: str):
        logs = self.repository_log.get_logs(road_width__lte=max_road_width, vehicle_type=vehicle_type)
        return TrafficLogDomainModel.asJSON(logs)

    def get_logs_near_toll_station(self, province: str, distance: int, toll_station_name: str, vehicle_type: str, minutes: int):

        station_query = self.repository_station.get_logs(name=toll_station_name)
        stations = TollDomainModel.asJSON(station_query)

        if stations == []:
            raise FileExistsError

        station = stations[0]
        station_location = (station['latitude'], station['longitude'])

        desired_date = timezone.now() - timezone.timedelta(minutes=minutes)
        print(desired_date)
        province_logs_by_type = self.repository_log.get_logs(vehicle_type=vehicle_type, province_name=province, date__gte=desired_date)
        # province_logs_by_type_json = TrafficLogDomainModel.asJSON(province_logs_by_type)

        results = []
        if province_logs_by_type is not None:
            for log in province_logs_by_type:
                log_location = (log.latitude, log.longitude)
                distance_from_stations = hs.haversine(log_location, station_location) * 1000
                if distance_from_stations < int(distance):
                    results.append(log)

        return TrafficLogDomainModel.asJSON(results)

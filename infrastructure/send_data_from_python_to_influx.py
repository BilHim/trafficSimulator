## tbased on : https://www.influxdata.com/blog/getting-started-python-influxdb/
## pip install influxdb
from influxdb import InfluxDBClient
import json
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('TrafficSimultionDB')
f = open('data_to_send.json')
json_body = json.load(f)
client.write_points(json_body)
# client.get_list_database()
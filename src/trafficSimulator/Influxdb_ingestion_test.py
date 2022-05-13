from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "sZfvJyJlyAyuMbv9bezFylG57DuDgz2gaMJgqNVzzHAqfV88S7Onr7hQy3VMl8qNzPiO667WHsn0tWwcjxHN-A=="
org = "test-org"
bucket = "tarffic-bucket"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    data = "mem,host=host1 used_percent=23.43234543"
    write_api.write(bucket, org, data)

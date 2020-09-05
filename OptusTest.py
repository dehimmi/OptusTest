#from influxdb import InfluxDBClient
#client = InfluxDBClient(host='localhost', port='8086')
#print(client.get_list_database())
#client.switch_database('pythondb')
#print(client.get_list_measurements())

import pytest


def test_pass():
    assert 1+1 == 2


#client.write_points(result, database='pythondb', time_precision='ms')

# python -m pytest test_example.py --pytest-influxdb --influxdb_host=localhost --influxdb_name=pythondb

# python -m pytest test_example.py --pytest-influxdb --influxdb_host=52.63.126.230 --influxdb_name=pythondb

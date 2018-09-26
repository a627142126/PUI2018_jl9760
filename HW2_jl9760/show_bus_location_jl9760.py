# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
apikey = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)

bus_total = dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
print("Bus Line : %s"%(bus_line))
print("Number of Active Buses : %s"%(len(bus_total)))
for i in range(0, len(bus_total)):
    longitude = bus_total[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = bus_total[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print("Bus %s is at latitude %s and longitude %s"%(i, latitude, longitude))
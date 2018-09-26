#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 02:41:05 2018

@author: apple
"""

from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python aPythonScriptThatWritesToCSV.py mycsv.csv")
    sys.exit()

apikey = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
fout = open(sys.argv[3], "w")
bus_total = dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(0, len(bus_total)):
    longitude = bus_total[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = bus_total[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    stop_name = bus_total[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    Stop_status = bus_total[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    fout.write("%s,%s,%s,%s\n"%(latitude, longitude, stop_name, Stop_status))
    
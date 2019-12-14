# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# rangerSEye_2k5_python_sample/main.py

import datetime
import sys
import connection

sys.path.append('rangerSEye_4m3') # search in rangerSEye_4m3 interface
import telemetryStateEvent_rangerseye_4m3 as rangerSEye_4m3_telemetry

# want to connect another device? just update the credentials below
SCOPE_ID = '0ne000A3590'
DEVICE_ID = 'gvxnpsn7rv64dawrlvegqc'
KEY = 'MsS/JTim0T4cs5rpjDF/Ry93uMRuVzPP/Nin0bczTpA='

gCounter = 0
gDevice = None

def callback(info): # iotc.IOTCallbackInfo
  global gDevice

  if gDevice == None:
    gDevice = info.getClient()

  if info.getEventName() == 'ConnectionStatus':
    if info.getStatusCode() == 0:
      if gDevice.isConnected():
        print(str(datetime.datetime.now()), 'Connected!')
        return
    print(str(datetime.datetime.now()), 'Connection Lost?')
    gDevice = None
    return

  if info.getEventName() == 'SettingsUpdated':
    print(str(datetime.datetime.now()), 'Received an update to device settings.')
# there was no device settings definition for the device

  if info.getEventName() == 'Command':
    print(str(datetime.datetime.now()), 'Received a C2D from cloud to device settings.')
# there was no C2D (cloud to device) definition for the device

def main():
  global gCounter, gDevice

  while True:
    gDevice = connection.Connect(SCOPE_ID, DEVICE_ID, KEY, callback)

    while gDevice != None and gDevice.isConnected():
      gDevice.doNext() # do the async work needed to be done for MQTT
      if gCounter % 10 == 0: # every 10 seconds
        gCounter = 0

        # sending telemetry for rangerSEye_4m3 interface
        print(str(datetime.datetime.now()), 'sending telemetry for rangerSEye_4m3 interface')
        rangerSEye_4m3_telemetry.Send(gDevice)

      gCounter += 1

main()

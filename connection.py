# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# rangerSEye_2k5_python_sample/connection.py

import sys
import iotc
from iotc import IOTConnectType, IOTLogLevel

def Connect(scope_id, device_id, key, callback):
  # create azure iot device instance
  device = iotc.Device(scope_id, key, device_id, IOTConnectType.IOTC_CONNECT_SYMM_KEY)
  device.setTokenExpiration(21600) # 6 hours
  device.setLogLevel(IOTLogLevel.IOTC_LOGGING_API_ONLY)

  # setup event callbacks
  device.on("ConnectionStatus", callback)
  device.on("MessageSent", callback)
  device.on("Command", callback)
  device.on("SettingsUpdated", callback)

  if device.connect() != 0:
    sys.exit(1)

  return device

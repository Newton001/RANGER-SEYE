# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# rangerSEye_2k5_python_sample/@rangerSEye_4m3/telemetryEventState.py

import json

def CreateBlob():
  return {
    'Fire': 'update here',
  }

def Send(device):
  device.sendTelemetry(json.dumps(CreateBlob()))

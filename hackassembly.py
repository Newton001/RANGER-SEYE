import serial
import sys
import urllib.request
from time import sleep
from urllib.request import urlopen, Request
import json,time
import RPi.GPIO as GPIO
from twilio.rest import Client

def arduino_data():
        ser = serial.Serial('/dev/ttyACM0',9600)
        read_serial=ser.readline()
        read_serial=float(read_serial)
        print (read_serial)
        return(read_serial)


def send_sms(message):
        message1=str(message)



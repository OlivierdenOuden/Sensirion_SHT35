#**********************************************************************************#
#														
#		SHT3x - Sensirion Temperature Humidity sensor	
#														
#		Read-out script.								
#														
#		Olivier den Ouden								
#		Royal Netherlands Meterological Institute		
#		RD Seismology and Acoustics						
#		https://www.seabirdsound.org 					
#														
#**********************************************************************************#

# Modules
import sht3x_main
import smbus
import time
from datetime import datetime
import numpy as np 
import argparse
from argparse import RawTextHelpFormatter

print('')
print('SHT3x Sensirion Temperature/Humidity sensor Read-out')
print('')
print('Olivier den Ouden')
print('Royal Netherlands Meteorological Institute, KNMI')
print('Dec. 2018')
print('')

# Parser arguments
parser = argparse.ArgumentParser(prog='SHT3x Sensirion Temperature/Humidity sensor Read-out',
    description=('Read-out of the SHT3x Sensirion sensor\n'
    ), formatter_class=RawTextHelpFormatter
)

parser.add_argument(
    '-t', action='store', default=100, type=float,
    help='Time of recording, [sec].\n', metavar='-t')

parser.add_argument(
    '-fs', action='store', default=1, type=float,
    help='Sample rate, [Hz].\n', metavar='-fs')

args = parser.parse_args()

# Check if MS can comunicate with SL
if lps33hw_main.init() == True:
	print "Sensor SHT3x initialized"
elif:
	print "Sensor SHT3x could not be initialized"
	exit(1)

# Time knowledge
st = datetime.utcnow()
fs = args.fs
record_t = args.t
n_samples = record_t*fs

# Save data
Time_array = np.linspace(0,record_t,n_samples)
Temp = np.zeros((n_samples,2))
Humi = np.zeros((n_samples,2))
Temp[:,0] = Time_array[:]
Pres[:,0] = Time_array[:]

# Loop 
i = 0
while i < n_samples:
	t_data,h_data = sht3x_main.read()
	Temp[i,1] = t_data
	Humi[i,1] = h_data
	i = i+1

	# Print converted data
	read_Humi,read_Temp = sht3x_main.pressure(t_data,h_data)
	print("Temp: %0.2f C  P: %0.2f % ") % (read_Temp,read_Humi)

	# Sampling rate
	time.sleep(1/fs)

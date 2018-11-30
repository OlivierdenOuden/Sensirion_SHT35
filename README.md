# Sensirion_SHT35

Read-out of the Sensirion SHT3x digital Temperature sensor by use of the I2C port on a Raspberry PI model 3B+. More info on the [SHT3x](http://www.mouser.com/ds/2/682/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital-971521.pdf) and the [I2C port](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial).

## Raspberry PI - I2C port 

First the hardware needs to be enabled before the software, attached python scripts, can be used. This is done by following the steps of the link above.
The I2C port is not enabled by default, this needs to be done;
1. Run, in terminal, ```sudo raspi-config```.
2. Select point 9, ```Advanced options```.
3. Select A7, ```I2C```, and select ```yes```.
4. Exit this window and reboot the PI.

After reboot, check if the I2C port is enabled by using;

```
ls /dev/*i2c*
```

if I2C port is open the PI will respond with;

```
/dev/i2c-1
```

where ```1``` indicates which I2C bus is used.

Now the I2C port is enabled but to have interaction between the PI and the sensor some utilities are needed. Use the following command line in a terminal;

```
sudo apt-get install -y i2c-tools
```

The ```i2cdetect``` command probes all the addresses on a I2C port bus, and report whether any devices are present. Outcome of this command, with the MS5837 sensor, will look like;

```
pi@raspberrypi:~/$ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Here the I2C adress of the sensor is 0x44. More information, or source, can be found [here](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial).

## I2C - Python 

To read out the sensors with python, some python modules are needed. Run the command lines below;

```
sudo apt-get update
sudo apt-get install python-smbus
sudo apt-get install python-obspy
```

## Python scripts - simple one shot data

The simple script includes a one-shot data request.

## Python scripts - src folder

The main file to read raw sensor data of the SHT3x is the ```sht3x_main.py``` script. This script includes all fuctions/defenitions needed to comunicate with the sensor. ```sht3x.py``` calls the main script and loops with a specific sampling rate. 

When starting ```sht3x.py```, one can ask for the help function (-h). This function shows the arguments one can give, with the script. Those arguments are:

```
-t            - Time of recording
-fs           - Sample rate
```

## Author

**Olivier den Ouden** - *KNMI* - [HFSP SeabirdSound](https://seabirdsound.org)

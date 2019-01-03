#!/usr/bin/env python3

import serial
import matplotlib.pyplot as plt
import numpy as np

# Plot definition
plt.style.use('ggplot')
plt.ion()
x = np.arange(143)
y = np.arange(143)
fig = plt.figure()
plt.xlim((0, 143))
plt.ylim((-300, 300))
ax = fig.add_subplot(111)
raw_curve, der_curve = ax.plot(x, y, 'r-', x, y, 'b-')

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200)
# Flush line
ser.readline()

# Infinite loop
while 1:
    packet = ser.readline().decode("utf-8")
    value = list(map(int, packet.split(',')))

    derivate_val = np.zeros(143)
    for index in range(1, 142):
        derivate_val[index] = value[index - 1] - value[index]

    raw_curve.set_data(x, value)
    der_curve.set_data(x, derivate_val)

    plt.pause(0.1)
    plt.draw()

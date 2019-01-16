import os
import time
import datetime
from w1thermsensor import W1ThermSensor

# Ambient probe ID: 021564e8b8ff 
# Waterproof probe ID: 0000075d075a
sensor = {
    'ambient': W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "021564e8b8ff"),
    'waterproof': W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0000075d075a")
}

#for sensor in (ambient, waterproof):
#    print(sensor.get_temperature(W1ThermSensor.DEGREES_F))

now = datetime.datetime.now().isoformat().replace('-', '').replace(':', '')[:13]
log = {
    'ambient': open('/home/msk/Projects/thermometer/ambient-{}.log'.format(now), 'w'),
    'waterproof': open('/home/msk/Projects/thermometer/waterproof-{}.log'.format(now), 'w')
}

while True:
    try:
        for k in ('ambient', 'waterproof'):
            t = int(time.time() * 1000)  # Javascript will use ms
            T = sensor[k].get_temperature(W1ThermSensor.DEGREES_F)
            log[k].write('{} {}\n'.format(t, T))
            log[k].flush()
        time.sleep(15)
    except:
        break

for k in ('ambient', 'waterproof'):
    log[k].close()

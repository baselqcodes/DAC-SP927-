import time
import numpy
import qcodes
import pyvisa as visa
import socket
from qcodes.dataset.measurements import Measurement
from qcodes.dataset.plotting import plot_dataset
from qcodes.instrument_drivers.Keysight.Keysight_34465A_submodules import Keysight_34465A

from qcodes import logger
from SP927v1 import SP927 # DAC
logger.start_all_logging
dac = SP927('LNHR_dac', "TCPIP0::192.168.0.5::23::SOCKET")
# import inspect
# print(inspect.getmro(type(dac)))
#print('Current DAC output: ' +  str(dac.channels[:].volt.get()))
dac.ch7.volt(4)
print('Current DAC output: ' +  str(dac.channels[:].volt.get()))
















































































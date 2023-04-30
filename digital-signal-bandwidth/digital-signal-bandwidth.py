#!/usr/bin/env python3

import numpy as np
from scipy import signal

import matplotlib.pyplot as plt

class DigitalSignal:
    def __init__(self, tstart, tend, drise, dfall, amplitude, povershoot, pundershoot):
        self._tstart = tstart
        self._tend = tend
        self._drise = drise
        self._dfall = dfall
        self.amplitude = amplitude
        self.povershoot = povershoot
        self.pundershoot = pundershoot
        self._wn = 1

    def get_damping(self, pxshoot):
        if pxshoot == 0:
            df = 0.5
        else:
            df = -np.log(pxshoot/100.0)/np.sqrt((np.pi^2)+(np.log(pxshoot/100.0)^2))

        return df

    def H(self, amplitude, wn, pxshoot):
        df = self.get_damping(pxshoot)
        lti = scipy.signal.lti([amplitude*(wn^2)], [1.0, 2*df*wn, wn^2])
        return lti

    def Hr(self):
        lti = self.H(self.amplitude, self._wn, self.povershoot)
        return lti

    def Hf(self):
        lti = self.H(self.amplitude, self._wn, self.pundershoot)
        return lti

def digital_signal()

lti = signal.lti([1], [1.0, 0.5, 1.0])

t, y = signal.step(lti, 0, np.linspace(0, 60, 2000))
t2, y2 = signal.step(lti, 0, np.linspace(0, 30, 1000))

y[1000:] -= y2

plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid()
plt.show()
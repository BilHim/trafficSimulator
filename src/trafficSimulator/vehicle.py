import numpy as np
from numpy.random import randint
import random

class Vehicle:
    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        # diff cars --- private car: 90%, trucks: 3%, motor-cycle: 7%
        r = randint(1, 100)
        r_speed = random.uniform(1,2)
        temp = randint(0,1)
        if(temp): r_speed *= -1
        if(r<=3):
            self.l = 8
            self.s0 = 6 # minimum desired distance between the vehicle i and i-1
            self.v_max = 5 + r_speed # maximum desired speed of the vehicle i
            self.a_max = 1.2 # maximum acceleration for the vehicle i.
            self.b_max = 3.90 # comfortable deceleration for the vehicle i.   
        if(r > 10):
            self.l = 4
            self.s0 = 4 # minimum desired distance between the vehicle i and i-1
            self.v_max = 6 + r_speed # maximum desired speed of the vehicle i
            self.a_max = 1.44 # maximum acceleration for the vehicle i.
            self.b_max = 4.61 # comfortable deceleration for the vehicle i.
        if(r > 3 and r <= 10):
            self.l = 2
            self.s0 = 2 # minimum desired distance between the vehicle i and i-1
            self.v_max = 7 + r_speed # maximum desired speed of the vehicle i
            self.a_max = 5 # maximum acceleration for the vehicle i.
            self.b_max = 4.90 # comfortable deceleration for the vehicle i.

        self.T = 1 # the reaction time of the i-th vehicle’s driver

        self.path = []
        self.current_road_index = 0

        self.x = 0
        self.v = self.v_max
        self.a = 0
        self.stopped = False
    
    def __repr__(self):
        return str(self.l)

    def init_properties(self):
        self.sqrt_ab = 2*np.sqrt(self.a_max*self.b_max)
        self._v_max = self.v_max

    def update(self, lead, dt):
        # Update position and velocity
        if self.v + self.a*dt < 0:
            self.x -= 1/2*self.v*self.v/self.a
            self.v = 0
        else:
            self.v += self.a*dt
            self.x += self.v*dt + self.a*dt*dt/2
        
        # Update acceleration
        alpha = 0
        if lead:
            delta_x = lead.x - self.x - lead.l
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T*self.v + delta_v*self.v/self.sqrt_ab)) / delta_x

        self.a = self.a_max * (1-(self.v/self.v_max)**4 - alpha**2)

        if self.stopped: 
            self.a = -self.b_max*self.v/self.v_max
        
    def stop(self):
        self.stopped = True

    def unstop(self):
        self.stopped = False

    def slow(self, v):
        self.v_max = v

    def unslow(self):
        self.v_max = self._v_max
        


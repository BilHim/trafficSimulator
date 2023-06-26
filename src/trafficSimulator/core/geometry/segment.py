from scipy.spatial import distance
from scipy.interpolate import interp1d
from collections import deque
from numpy import arctan2, unwrap, linspace
from abc import ABC, abstractmethod
from math import sqrt
from scipy.integrate import quad

class Segment(ABC):
    def __init__(self, points):
        self.points = points
        self.vehicles = deque()

        self.set_functions()
        

    def set_functions(self):
        # Point
        self.get_point = interp1d(linspace(0, 1, len(self.points)), self.points, axis=0)
        
        # Heading
        headings = unwrap([arctan2(
            self.points[i+1][1] - self.points[i][1],
            self.points[i+1][0] - self.points[i][0]
        ) for i in range(len(self.points)-1)])
        if len(headings) == 1:
            self.get_heading = lambda x: headings[0]
        else:
            self.get_heading = interp1d(linspace(0, 1, len(self.points)-1), headings, axis=0)

    def get_length(self):
        length = 0
        for i in range(len(self.points) -1):
            length += distance.euclidean(self.points[i], self.points[i+1])
        return length

    def add_vehicle(self, veh):
        self.vehicles.append(veh.id)

    def remove_vehicle(self, veh):
        self.vehicles.remove(veh.id)

    @abstractmethod
    def compute_x(self, t):
        pass
    @abstractmethod
    def compute_y(self, t):
        pass
    @abstractmethod
    def compute_dx(self, t):
        pass
    @abstractmethod
    def compute_dy(self, t):
        pass

    def abs_f(self, t):
        return sqrt(self.compute_dx(t)**2 + self.compute_dy(t)**2)
    
    def find_t(self, a, L, epsilon):
        """  Finds the t value such that the length of the curve from a to t is L.

        Parameters
        ----------
        a : float
            starting point of the integral
        L : float
            target length
        epsilon : float
            precision of the approximation
        """
        
        def f(t):
            integral_value, _ = quad(self.abs_f, a, t)
            return integral_value
        
        # if we cannot reach the target length, return 1 
        if f(1) < L: return 1
        
        lower_bound = a
        upper_bound = 1
        mid_point = (lower_bound + upper_bound) / 2.0
        integ = f(mid_point)
        while abs(integ-L) > epsilon:
            if integ < L:       lower_bound = mid_point
            else:               upper_bound = mid_point
            mid_point = (lower_bound + upper_bound) / 2.0
            integ = f(mid_point)
        return mid_point
    
    def find_normalized_path(self, CURVE_RESOLUTION=50):
        normalized_path = [(self.compute_x(0), self.compute_y(0))]
        l = self.get_length()
        target_l = l/(CURVE_RESOLUTION-1)
        epsilon = 0.01
        a = 0
        for i in range(CURVE_RESOLUTION-1):
            t = self.find_t(a, target_l, epsilon)
            new_point = (self.compute_x(t), self.compute_y(t))
            normalized_path.append(new_point)
            if t == 1: break
            else:      a = t
        return normalized_path
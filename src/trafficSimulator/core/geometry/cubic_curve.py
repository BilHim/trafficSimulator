from .segment import Segment
from math import sqrt
from scipy.integrate import quad

CURVE_RESOLUTION = 50

class CubicCurve(Segment):
    def __init__(self, start, control_1, control_2, end):
        # Store characteristic points
        self.start = start
        self.control_1 = control_1
        self.control_2 = control_2
        self.end = end

        # Generate path
        path = []
        for i in range(CURVE_RESOLUTION):
            t = i/CURVE_RESOLUTION
            x = t**3*self.end[0] + 3*t**2*(1-t)*self.control_2[0] + 3*(1-t)**2*t*self.control_1[0] + (1-t)**3*self.start[0]
            y = t**3*self.end[1] + 3*t**2*(1-t)*self.control_2[1] + 3*(1-t)**2*t*self.control_1[1] + (1-t)**3*self.start[1]
            path.append((x, y))

        super().__init__(path)
        # Arc-length parametrization
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
        super().__init__(normalized_path)

    def compute_x(self, t):
        return t**3*self.end[0] + 3*t**2*(1-t)*self.control_2[0] + 3*(1-t)**2*t*self.control_1[0] + (1-t)**3*self.start[0]
    def compute_y(self, t):
        return t**3*self.end[1] + 3*t**2*(1-t)*self.control_2[1] + 3*(1-t)**2*t*self.control_1[1] + (1-t)**3*self.start[1]
    def compute_dx(self, t):
        return 3*t**2*(self.end[0]-3*self.control_2[0]+3*self.control_1[0]-self.start[0]) + 6*t*(self.control_2[0]-2*self.control_1[0]+self.start[0]) + 3*(self.control_1[0]-self.start[0])
    def compute_dy(self, t):
        return 3*t**2*(self.end[1]-3*self.control_2[1]+3*self.control_1[1]-self.start[1]) + 6*t*(self.control_2[1]-2*self.control_1[1]+self.start[1]) + 3*(self.control_1[1]-self.start[1])
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
        
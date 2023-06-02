from .segment import Segment

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
        normalized_path = self.find_normalized_path(CURVE_RESOLUTION)
        super().__init__(normalized_path)


    def compute_x(self, t):
        return t**3*self.end[0] + 3*t**2*(1-t)*self.control_2[0] + 3*(1-t)**2*t*self.control_1[0] + (1-t)**3*self.start[0]
    def compute_y(self, t):
        return t**3*self.end[1] + 3*t**2*(1-t)*self.control_2[1] + 3*(1-t)**2*t*self.control_1[1] + (1-t)**3*self.start[1]
    def compute_dx(self, t):
        return 3*t**2*(self.end[0]-3*self.control_2[0]+3*self.control_1[0]-self.start[0]) + 6*t*(self.control_2[0]-2*self.control_1[0]+self.start[0]) + 3*(self.control_1[0]-self.start[0])
    def compute_dy(self, t):
        return 3*t**2*(self.end[1]-3*self.control_2[1]+3*self.control_1[1]-self.start[1]) + 6*t*(self.control_2[1]-2*self.control_1[1]+self.start[1]) + 3*(self.control_1[1]-self.start[1])

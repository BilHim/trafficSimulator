from .segment import Segment

PAS = 0.01
CURVE_RESOLUTION = 50

class QuadraticCurve(Segment):
    def __init__(self, start, control, end):
        # Store characteristic points
        self.start = start
        self.control = control
        self.end = end

        # Generate path
        path = []
        for i in range(CURVE_RESOLUTION):
            t = i/(CURVE_RESOLUTION-1)
            x = t**2*self.end[0] + 2*t*(1-t)*self.control[0] + (1-t)**2*self.start[0]
            y = t**2*self.end[1] + 2*t*(1-t)*self.control[1] + (1-t)**2*self.start[1]
            path.append((x, y))

        super().__init__(path)

        # Arc-length parametrization
        normalized_path = self.find_normalized_path(CURVE_RESOLUTION)
        super().__init__(normalized_path)

    def compute_x(self, t):
        return t**2*self.end[0] + 2*t*(1-t)*self.control[0] + (1-t)**2*self.start[0]
    def compute_y(self, t):
        return t**2*self.end[1] + 2*t*(1-t)*self.control[1] + (1-t)**2*self.start[1]
    def compute_dx(self, t):
        return 2*t*(self.end[0]-2*self.control[0]+self.start[0]) + 2*(self.control[0]-self.start[0])
    def compute_dy(self, t):
        return 2*t*(self.end[1]-2*self.control[1]+self.start[1]) + 2*(self.control[1]-self.start[1])
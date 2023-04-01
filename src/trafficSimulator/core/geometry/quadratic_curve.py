from .segment import Segment

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

        # Arc-length parametrization
        # TODO

        # Initialize super
        super().__init__(path)

import numpy as np
from svgpathtools import parse_path

POINTS_PER_UNIT_DISTANCE = 2

class Path:
    def __init__(self, path_string):
        '''
        Constructs a path using an SVG-style string.

                Parameters:
                ----------
                        path_string (str): SVG-style path string.
        '''
        self.path_object = parse_path(path_string)

    def length(self):
        '''Returns the length of the path.'''
        return self.path_object.length()
        
    def point(self, t):
        '''
        Returns a point along the path.

                Parameters:
                ----------
                        t (float): Progress along the path. 0=start, 1=end.

                Returns:
                -------
                        point (np.array): The point along the path.
        '''

        p = self.path_object.point(t)
        return np.array([p.real, p.imag])

    def path(self, n=None):
        '''
        Returns a numpy.array of points representing the path.

                Parameters:
                ----------
                        n (int): Number of points. Defaults to the length of the path times `POINTS_PER_UNIT_DISTANCE`.

                Returns:
                -------
                        points (np.array): Array of points representing the path.
        '''

        if n is None:
            n = int(self.length() * POINTS_PER_UNIT_DISTANCE) + 1

        points = [self.point(i/n) for i in range(n+1)]
        return np.array(points)
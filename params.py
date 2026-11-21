#parameters

class P:
    def __init__( self, 
                 g: float = 9.82, #gravitational constant m/s^2
                 L: float = 0.50, #length of pendulum [m]
                 m: float = 0.05, #mass of bob [kg]
                 b: float = 0.0, #Linear dampening [N * s / s]
                 h0: float = 0.00, #gap between plate and bob at the bottom of swing [m]
                 Ap: float = 0.0, #plate amplitude [m]
                 wd: float = 0.0 #plate angular frequency
                 ):
        
        self.g = g
        self.L = L
        self.m = m
        self.b = b
        self.h0 = h0
        self.Ap = Ap
        self.wd = wd

    
import numpy as np
from params import P

def plate_velocity(t,p):
    return p.Ap * p.wd * np.cos(p.wd * t)

def eddy_force(theta, omega, t, p):
    #Simplified electromagnetic force from eddy currents in conductive plate

    v_bob = p.L * omega
    return -p.b * (v_bob - plate_velocity(t, p))

def fun(t, initial_conditions, p): #differential equation that gets passed into solve_ivp
    theta, omega = initial_conditions

    torque = (-p.m * p.g * p.L * np.sin(theta) 
              + p.L * eddy_force(theta, omega, t, p))
    
    #returns theta double dot and theta dot
    return [omega, torque/(p.m * p.L**2)]


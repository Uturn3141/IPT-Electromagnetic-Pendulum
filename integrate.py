import numpy as np
from scipy.integrate import solve_ivp
from model import fun

def run(p, y0, t_end, dt = 1e-3, rtol = 1e-10, atol=1e-12):
    #rtol is relative tolerance, atol is absolute tolerance
    #integrate from t = 0 to t_end 

    t_eval = np.arange(0.0, t_end, dt)
    sol = solve_ivp(fun, (0.0, t_end), y0, args=(p,), method="DOP853",
                    rtol=rtol, atol=atol, t_eval=t_eval)

    return sol

def energy(sol, p):
    #E = T + U
    theta, omega = sol.y
    return 0.5 * p.m * p.L**2 * omega**2 + p.m * p.g * p.L * (1-np.cos(theta))


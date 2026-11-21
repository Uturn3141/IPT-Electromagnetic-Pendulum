import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from params import P
from integrate import run, energy

def underdamped():
    p = P()
    #[1.0, 0.0] identifies initial conditions: theta0 and omega0
    #sol.y[0] returns the first variable defined in initial conditions
    sol = run(p, [1.0, 0.0], t_end = 20)
    fig, ax = plt.subplots(1, 2, figsize=(10,3.5))
    ax[0].plot(sol.t, sol.y[0])
    ax[0].set(xlabel="t (s)", ylabel = "theta rad", title="underdamped")
    
    E = energy(sol, p)
    #plotting energy drift
    ax[1].plot(sol.t, (E - E[0])/E[0])
    ax[1].set(xlabel="t (s)", ylabel="relative energy drift", title="energy drift")
    
    fig.tight_layout()

def dampened_case():
    p=P(b=0.005)
    theta0 = 0.5
    sol = run(p, [theta0, 0.0], t_end = 100)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(sol.t, sol.y[0], label="simulation")

    envelope = theta0*np.exp(-p.b * sol.t/(2*p.m))
    ax.plot(sol.t, envelope, "k--", label="theta0 * e^((-b/2m)*t)")
    ax.plot(sol.t, -envelope, "k--")
    ax.set(xlabel = "t (s)", ylabel = "theta", title="damped harmonic oscillator, stationary plate, with theoretical amplitude envelope")
    ax.legend()
    fig.tight_layout()


def driven_case():
    p = P(Ap=0.01, b = 0.005)
    #set value of plates oscillations,
    #in this case, it is some percent of the natural frequency
    p.wd = 0.455 * np.sqrt(p.g/p.L)

    theta0 = 0.0
    sol = run(p, [theta0, 0.0], t_end = 150)
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(sol.t, sol.y[0], label="bob angle")
    ax.plot(sol.t, p.Ap/p.L * np.sin(p.wd*sol.t), label="plate position/L")
    ax.set(xlabel = "t (s)", ylabel = "theta", title="driven case with plate position")
    ax.legend()
    fig.tight_layout()

if __name__ =="__main__":
    underdamped()
    dampened_case()
    driven_case()
    plt.show()

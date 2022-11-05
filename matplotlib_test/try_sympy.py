
import math
from sympy import *

a_mult = 3
b_mult = 4
a = Symbol('a')


print("What is", a_mult, "*", a, "+", b_mult, "*", a)
expr = str((a_mult * a + b_mult * a)/2).replace("*", "")

init_printing(use_unicode=True)

pprint(expr)


import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True


t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(t, s)

ax.set_xlabel(r'\textbf{time (s)}')
ax.set_ylabel('\\textit{Velocity (\N{DEGREE SIGN}/sec)}', fontsize=16)
ax.set_title(r'\TeX\ is Number $\displaystyle\sum_{n=1}^\infty'
             r'\frac{-e^{i\pi}}{2^n}$!', fontsize=16, color='r')

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import math

v0 = 170
ts = np.arange(0,2,0.01)
vs = v0 *np.sin(2*np.pi*ts)
ts.size==vs.size
fig, ax=plt.subplots()

ax.plot(ts,vs)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

Pob= np.array([6, 6+7, 6+7+8, 6+7+8+9, 6+7+8+9+10, 6+7+8+9+10+12,6+7+8+9+10+12+12,6+7+8+9+10+12+12+12,
6+7+8+9+10+12+12+12+12, 6+7+8+9+10+12+12+12+12+12])
Wealth=np.array(range(10,101,10))
plt.plot(Pob, Wealth)
plt.plot([0,100], [0,100])
plt.plot()
plt.show()
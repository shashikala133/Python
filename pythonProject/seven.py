import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
from matplotlib.pyplot import plot


def s(flib=2):
    x=np.linespace(0,14,100)
    for i in range (1,5):
        plt,plot(x.np.sin(x+i*.5)*(7-i)*flib)
sb.set()
s()
plt.show()

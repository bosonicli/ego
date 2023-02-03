# %% [markdown]
# # Test Jupyter

# %% [markdown]
# ## test shell interactive

# %%
!ls
!pwd

# %% [markdown]
# ## test init

# %%
os.getcwd()
%matplotlib widget

# %% [markdown]
# ## test import

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display

# %% [markdown]
# ## test canvas setting

# %%
fig1 = plt.figure()
ax1 = plt.axes(projection = '3d')

# %% [markdown]
# ## test curve setting

# %%
theta1 = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z1 = np.linspace(-2, 2, 100)
r1 = z1**2 +1
x1 = r1 * np.sin(theta1)
y1 = r1 * np.cos(theta1)

# %% [markdown]
# ## test curve show

# %%
ax1.plot(x1, y1, z1, label='parametric curve')
ax1.legend()

plt.show()

# %% [markdown]
# ## test Jupyter interactive

# %%
def testSlider(x):
    return x
# generate a slider
interact(testSlider, x=widgets.IntSlider(min=0, max=20, step=1, value=10));
interact(testSlider, x=widgets.Combobox(options=["Chicago", "New York", "Washington"], value="Chicago"));

def sumInteractive(a, b):
    display(a + b)
    return a+b
w = interactive(sumInteractive, a=10, b=20)
display(w)



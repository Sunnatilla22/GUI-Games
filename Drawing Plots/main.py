import pandas as pd

import matplotlib.pyplot as plt


# air_quality = pd.read_csv("air_quality.csv")
# air_quality.head()
# air_quality.plot()
# plt.show()

# cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
# dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
# activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
#
# fig, ax = plt.subplots()
# ax.plot(activity, dog, label="dog")
# ax.plot(activity, cat, label="cat")
# ax.legend()
#
# plt.show()

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
import matplotlib.markers
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

# plt.plot(ypoints, marker="o")
# plt.plot(ypoints, marker=matplotlib.markers.CARETDOWN)
# 例如 o:r，o 表示实心圆标记，: 表示虚线，r 表示颜色为红色。
# plt.plot(ypoints, 'o:r')

# markersize，简写为 ms：定义标记的大小。
# markerfacecolor，简写为 mfc：定义标记内部的颜色。
# markeredgecolor，简写为 mec：定义标记边框的颜色。
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r',mfc='y')
plt.show()
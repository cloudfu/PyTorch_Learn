import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("test")

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()
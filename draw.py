import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt 
import numpy as np                # 导入模块 numpy，并简写成 np

x = np.linspace(-50, 50, 5000)
y = np.sin(x)

y1 = 4*x**2 + 5*x + 6    #二次函数
y2 = np.exp(x)     #指数



plt.plot(x, y)

plt.figure()
plt.plot(x, y1)

plt.figure()
plt.plot(x, y2)






plt.show()

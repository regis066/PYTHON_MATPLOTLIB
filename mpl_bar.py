from matplotlib import pyplot as plt
import numpy as np 
# print(plt.style.available)
plt.style.use('fivethirtyeight')
# plt.xkcd()

age_x = [25,26,27,28,29,30,31,32,32,33,34]
x_indexes = np.arange(len(age_x))
width = 0.25 
dev_y = [184960, 220000, 267520, 393200 , 432000, 560000, 62316, 34928, 273117, 18748, 13752]

plt.bar(x_indexes - width, dev_y, color='#444444' , linestyle= '--',  label= "All Dev" , width=width)

py_dev_y = [42300, 46852, 49320 , 54200, 58000, 62516, 64828, 675117, 68948, 73952, 80000]
plt.bar(x_indexes , py_dev_y, label = "Python Dev", width=width)

js_dev_y = [37810, 43515, 46823, 49293, 53437,56373,62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width , js_dev_y , label = "JS Dev", width=width)


plt.legend()
plt.xticks(ticks=x_indexes , label=age_x)
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")
plt.title('Median Salary (USD) by Age')
plt.grid(True)
plt.tight_layout()
plt.show()
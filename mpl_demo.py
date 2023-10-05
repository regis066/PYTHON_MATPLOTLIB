from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use('fivethirtyeight')
plt.xkcd()

age_x = [25,26,27,28,29,30,31,32,32,33,34]
dev_y = [38496, 42000, 46752, 49320 , 53200, 56000, 62316, 64928, 673117, 68748, 73752]

plt.plot(age_x, dev_y, color='#444444' , linestyle= '--',  label= "All Dev" )

py_dev_y = [42300, 46852, 49320 , 54200, 58000, 62516, 64828, 675117, 68948, 73952, 80000]
plt.plot(age_x , py_dev_y, label = "Python Dev")

js_dev_y = [37810, 43515, 46823, 49293, 53437,56373,62375, 66674, 68745, 68746, 74583]
plt.plot(age_x , js_dev_y , label = "JS Dev")


plt.legend()
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")
plt.title('Median Salary (USD) by Age')
plt.grid(True)
plt.tight_layout()
plt.show()
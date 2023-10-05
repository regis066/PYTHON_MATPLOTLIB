from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

# slices = [120, 80, 30, 20 ]
# labels = ["oneTwenty" , "Eighty","thirty", "twenty" ]
# colors = ["#008fd5" , "#fc4f30", "#E5ae37", "#6d904f"]

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0 , 0 , 0.1 , 0 ]

plt.pie(slices, labels=labels, explode=explode , shadow=True ,autopct="%1.1f%%" ,  wedgeprops={'edgecolor': 'black'})


plt.tight_layout()
plt.show()
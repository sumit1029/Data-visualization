import matplotlib.pyplot as plt

a = [1, 2, 3, 4]    #Values
b = [2, 4, 6, 8]    #Doubles

plt.title("Line chart")   #Title of chart
plt.xlabel("Values")    #X-azis name
plt.ylabel("Double")    #Y-axis name

plt.plot(a, b, 'r', linestyle = 'dashed', marker = '.', label = 'A simple line')
plt.legend(loc = 'lower right')  #Location of labels
plt.show()
import matplotlib.pyplot as plt

a = [3, 5, 8, 9]
name = ['Java', 'C++', 'Python', 'Javascript']

plt.title("Languages popularity")

plt.pie(a, labels=name, autopct="%1.1f%%")
plt.show()
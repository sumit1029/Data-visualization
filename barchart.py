import matplotlib.pyplot as plt

a = ['Java', 'C++', 'C', 'Python', 'Javascript']
b = [8, 6, 4, 9, 9.6]

plt.title("Languages ratings")
plt.xlabel("Languages")
plt.ylabel("Ratings")

plt.bar(a, b)
plt.show()
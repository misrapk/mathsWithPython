import matplotlib.pyplot as plt
nyTemp = [56.9,56.3,56.4,55.7,53.4,55.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]

years = range(2000, 2014)

plt.plot(years, nyTemp, marker='o')
plt.show()
import matplotlib.pyplot as plt
with open('filename.csv', 'r') as f:
    lines = f.readlines()

# a is append
# w is write (which replaces the content of the file)
x = []
y = []
for line in lines:
    parts = line.split(',')
    x.append(float(parts[0]))
    y.append(float(parts[1]))

plt.plot(x, y)
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.title('Title')
plt.show()



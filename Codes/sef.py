# import matplotlib.pyplot as plt
#
# # Sample data
# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]
#
# # Plotting the data
# plt.plot(x, y)
#
# # Display the plot
# plt.show()

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Plotting with labels
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x²')

# Adding title and labels
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Quadratic Plot")

# Show legend
plt.legend()

# Display the plot
plt.show()

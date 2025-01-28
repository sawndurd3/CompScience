import numpy as np
import matplotlib.pyplot as plt

# DATA
weight = np.array([140, 155, 159, 179, 192, 200, 212])
height = np.array([60, 62, 67, 70, 71, 72, 75])

# FUNCTION
def calculateSlopeAndIntercept(weights, heights): 
    n = len(weights)
    totalX = sum(weights)
    totalY = sum(heights)
    totalXY = sum(list(map(lambda x, y: x * y, weights, heights)))
    totalXSquared = sum(list(map(lambda x: x * x, weights)))
    totalXthenSquared = totalX * totalX

    # FORMULA FOR SLOPE
    slope = ((n * totalXY) - (totalX * totalY)) / ((n * totalXSquared) - totalXthenSquared)
    # FORMULA FOR INTERCEPT
    intercept = (totalY - (slope * totalX)) / n

    print(f"Slope: {slope} \nIntercept: {intercept}")
    return slope, intercept

b, a = calculateSlopeAndIntercept(weight, height)

regression = a + b * weight

# PLOT DATA POINTS
plt.scatter(weight, height, color='blue', marker='x', label='Data points')

# PLOT REGRESSION LINE
plt.plot(weight, regression, color='red', label=f'Regression Line')

plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

plt.xlabel('Weight (lbs)')
plt.ylabel('Height (inches)')
plt.title('Linear Regression Model: Height vs Weight')
plt.legend()
plt.show()

import numpy as np 
from sklearn.neighbors import KNeighborsRegressor

class Point:
    def __init__(self):
        print("Please input real numbers x, y for point(x, y):")
        self.x, self.y = map(np.float, input().split())


print("Please input an positive number N:")
N = np.int(input())
print(f"Your input N is: {N}")

print("Please input an positive number k:")
k = np.int(input())
print(f"Your input k is: {k}")

train_data_x = []
train_data_y = []
for _ in range(N):
    point = Point()
    train_data_x.append(point.x)
    train_data_y.append(point.y)

train_data_x = np.array(train_data_x).reshape(-1, 1) # 1d feature needs reshape to -1, 1
train_data_y = np.array(train_data_y).reshape(-1, 1)

knn = KNeighborsRegressor(k)
knn.fit(train_data_x, train_data_y)

print("Please input an number X:")
X = np.array([np.float(input())]).reshape(-1, 1)
print(f"Your input X is: {X}")

if k <= N:
    y_pred = knn.predict(X)
    print(y_pred)
else:
    print("Error: k is greater than N.")
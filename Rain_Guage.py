import matplotlib.pyplot as plt

data = [82.6, 102.9, 180.3, 110.3, 98.8, 136.7]
data = [82.6, 102.9, 180.3, 110.3, 98.8, 136.7]

m = len(data)
mean = sum(data) / m

print(f"mean : {mean}")

sqr_sum = sum((mean - i) ** 2 for i in data)
sig = (sqr_sum / (m - 1)) ** 0.5
print(f"sigma : {sig}")

cv = sig * 100 / mean
print(f"cv is : {cv}")

e = cv / (m ** 0.5)
print(f"Standard Error (e): {e}")

n = (cv / 10) ** 2
print(f"Required Sample Size (n): {n}")
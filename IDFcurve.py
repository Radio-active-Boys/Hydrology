import matplotlib.pyplot as plt

rainfall_duration = [1, 3, 6, 9, 12, 15, 18, 24]  

print(rainfall_duration)

conver_ration = [0.425,0.6,0.725,0.790,0.845,0.895,0.935,1]

hour_depth_24 = [192,212,232]
hour_24 = {(25,192),(50,212),(100,232)}

return_24 = [(hour_depth_24[0]*conver_ration[i])/rainfall_duration[i] for i in range(0,len(conver_ration))]
return_50 = [(hour_depth_24[1]*conver_ration[i])/rainfall_duration[i] for i in range(0,len(conver_ration))]
return_100 = [(hour_depth_24[2]*conver_ration[i])/rainfall_duration[i] for i in range(0,len(conver_ration))]

print("Return 24-year:", return_24)
print("Return 50-year:", return_50)
print("Return 100-year:", return_100)

plt.plot(rainfall_duration, return_24, 'b', label='24-year')
plt.plot(rainfall_duration, return_50, 'g', label='50-year')
plt.plot(rainfall_duration, return_100, 'r', label='100-year')

plt.xlabel('Rainfall Duration (hours)')
plt.ylabel('Return Period Intensity')
plt.title('Intensity-Duration-Frequency (IDF) Curves')
plt.legend()
plt.show()
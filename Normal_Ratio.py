P_ann_rain = [75,59,86]
N_mean_anul_rain = [750,650,850]

Pa = sum(P_ann_rain)/len(P_ann_rain)
Na = 700
if (abs(Na - i)/Na > 10 for i in N_mean_anul_rain):
    Pa = (700 / len(P_ann_rain)) * sum((P_ann_rain[i] / N_mean_anul_rain[i]) for i in range(len(P_ann_rain)))

print(Pa)
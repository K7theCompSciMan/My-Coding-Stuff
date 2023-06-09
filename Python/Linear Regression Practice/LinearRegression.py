import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
import os

def best_fit_line(xs, ys):
    slope = (((mean(xs) * mean(ys)) - mean(xs*ys)) / ((mean(xs) * mean(xs)) - mean(xs*xs)))
    y_intercept = mean(ys)-slope * mean(xs)
    return slope, y_intercept

filename = os.path.join('Python', 'Linear Regression Practice', 'weight-height.csv')
df = pd.read_csv(filename)
male_df = df[df['Gender']=='Male'][:200]
male_df['Height']=male_df['Height'].apply(lambda x:x*2.54)
male_df['Weight']=male_df['Weight'].apply(lambda x:x*0.45359237)


height_list = male_df['Height'].tolist()
weight_list = male_df['Weight'].tolist()
xs = np.array(height_list, dtype=np.float64)
ys = np.array(weight_list, dtype=np.float64)

slope, y_intercept = best_fit_line(xs, ys)
regression_line = [slope * x + y_intercept for x in xs]
average_man_height = mean(xs)
average_man_weight = ((slope * average_man_height) + y_intercept)

style.use('seaborn')
plt.scatter(xs,ys,label='Data Points', alpha=0.6, color='green', s=75)
plt.scatter(average_man_height, average_man_weight, label='Average Man', color='red', s=80)
plt.plot(xs, regression_line, label="Best Fit Line", color = 'orange', linewidth=4)
plt.title('Linear Regression of Height and Weight ')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()

plt.show()
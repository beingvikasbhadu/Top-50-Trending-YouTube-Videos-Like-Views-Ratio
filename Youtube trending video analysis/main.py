from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import data      # so data would be updated

# read csv file using pandas
data=pd.read_csv('data.csv')

# Create labels and title
plt.style.use('seaborn')
plt.title('Top 50 Popular Youtube Video in India')
plt.xlabel('View Count')
plt.ylabel("Likes")

plt.scatter(data['views'],data['likes'],edgecolor='black',c=data['ratio'],s=80,cmap='summer',linewidth=1)
cbar=plt.colorbar()
cbar.set_label('Likes/Views')

# scaling for X-axis values
plt.xscale('log',base=10)

plt.tight_layout()
plt.show()

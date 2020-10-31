import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Southern Oscillation Index (SOI)
#fig = plt.figure(figsize=(10,7))
df = pd.read_csv('C:/Users/user/Desktop/test.csv')


#df['Date'][0:2] = pd.to_datetime(df['Date'][0:2])



#ax = fig.add_subplot(1,1,1)
x_values = df['Date']
y_values = df['Value']
plt.plot(x_values,y_values)
plt.show()
#ax.plot(x_values,y_values) 

#plt.show()




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults


#Southern Oscillation Index (SOI)
fig = plt.figure(figsize=(20,12)) ############### fig 사이즈 ##############

df = pd.read_csv('SOI.csv',sep=',')#값 불러오기
data_ARIMA = pd.read_csv('SOI.csv',sep=',', header=0, parse_dates=True) #값 불러오기

df['Date'] = pd.to_datetime(df['Date'])
data_ARIMA = data_ARIMA['Value'] # 데이터 입력
data_ARIMA_cut = data_ARIMA#.iloc[0:700,] #데이터 700까지만 추출
data_ARIMA_cut.tail() #데이터 자름


model = ARIMA(data_ARIMA_cut, order = (1,1,0)) #ARIMA(1,1,0)을 따름
model_fit = model.fit(trend = 'nc', full_output = True, disp = 1)
#print(model_fit.summary())########## 모델 정확도 파악#####################
model_fit.plot_predict() ########### 모델 출력 ##############x축좀.. 하..

#fore = model_fit.forecast(steps = )
#print(fore)

plt.title('Southern Oscillation Index (SOI) Prediction')
plt.axhline(y=0,color='r')
plt.legend(['Prediction', 'Value']) 
########### 여기까지 예측##################

plot_acf(data_ARIMA_cut)
plot_pacf(data_ARIMA_cut) ################### 여기까지 AR MA ###################


ax = fig.add_subplot(1,1,1)
ax.set(title = 'Southern Oscillation Index (SOI)')
x_values = df['Date']
y_values = df['Value']
ax.axhline(y=0,color='r')
ax.plot(x_values,y_values,linewidth = 1)  ######### 
plt.show()##### 출력 #######

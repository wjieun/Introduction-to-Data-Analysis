
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


weather_df = pd.read_csv('data/weather_processed.csv')
station_df = pd.read_csv('data/station.csv')
location_df = pd.read_csv('data/location.csv', index_col='name')
distance_df = pd.read_csv('data/distance.csv', index_col='name')

location_df['estim_temp'] = np.nan  # location_df에 비어있는 예상 온도 column 생성
# location_df['estim_temp'] 채워 넣을 것
def weight(x):
	return 1 / (x ** 2)

date_time = input()
df1 = weather_df[weather_df['date_time'] == date_time]
df1 = df1.set_index('station_name')

distance_df = distance_df.apply(weight)
location_df['estim_temp'] = (distance_df * df1['temperature']).sum(axis=1) / distance_df.sum(axis=1)

check_location = input()
print(f"{location_df.loc[check_location, 'estim_temp']:.2f}°C")

show_temp_map = True  # False로 바꿀 시 실행 시간을 줄일 수 있음

if show_temp_map:
	# 한국 지도 그리기
	img = plt.imread('data/skorea2.png')
	plt.figure(figsize=(131.3 - 124.3, 38.7 - 32.8))
	plt.tight_layout()
	plt.xlim(124.3, 131.3)
	plt.ylim(32.8, 38.7)
	plt.imshow(img, aspect='auto', extent=[124.3, 131.3, 32.8, 38.7])
	plt.grid()

	# 산점도로 읍/면/동 온도 찍기 + 온도를 색깔로 사용
	plt.scatter(location_df['longitude'], location_df['latitude'], c=location_df['estim_temp'],
							cmap='coolwarm', marker='o', alpha=1.0)
	plt.colorbar(label='temperature')
	
	# 기상 관측소 위치 찍기
	plt.scatter(station_df['longitude'], station_df['latitude'], c='green', marker="*", label="station location")
	
	plt.legend()
	plt.savefig('out.png')
	plt.show()
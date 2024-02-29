import requests
from bs4 import BeautifulSoup
import datetime

f = open('page.txt', 'r', encoding='utf-8')
u = f.read()
f.close()
soup = BeautifulSoup(u, "html.parser")

time_elements = soup.find_all("span", class_="bg-orangeOne")

total_duration = datetime.timedelta()
# lst=['10:20', '15:30', '5:10', '10:30']# 41:30
c=0
for time_element in time_elements:
    time_str = time_element.text
    c+=1
    time_parts = time_str.split(":")
    minutes = int(time_parts[0])
    seconds = int(time_parts[1])
    duration = datetime.timedelta(minutes=minutes, seconds=seconds)
    total_duration += duration
    print(f'{c}')
    print(f'time={time_parts}')
    print(f'duration={duration}')
    print(f'Total_duration={total_duration}')
    print('--------------')
print("Total duration:", total_duration)
print("Total duration in hours, minutes, seconds:", total_duration.total_seconds() // 3600, "hours",
      (total_duration.total_seconds() // 60) % 60, "minutes",
      total_duration.total_seconds() % 60, "seconds")
import pandas as pd
import numpy as np

def main():
   df = pd.read_csv("data.csv")
   # print(df)

   dict_array  = turn_data_into_dict(df)

   print(dict_array)
   # pass_roundabout = []

   # row = len(df)

   # for i in range(row):
   #    time = df["Time"]
   #    distance = df["Distance"]
   #    speed = df["Speed"]
   #    lap = df["Lap"]
   #    sector = df["Sector"]
   #    break_time = df["Brake Times"]
   #    map_crashed = df["Map Crashed"]
   #    car_crashed = df["Car Crashed"]
   #    passed_roundabout = df["Passed Circus"]
   #    passed_crosswalk = df["Passed Crosswalk"]
   #    car_overturned = df["Car Overturned"]

      # pass_roundabout.append(passed_roundabout)
   # passed_roundabout = df["Passed Circus"]
   # speed = df["Speed"]
   # pass_roundabout_array = np.array(passed_roundabout)
   # speed_array = np.array(speed)

   # print(speed_array)
   # print(pass_roundabout_array)

def turn_data_into_dict(data):
   dict = {}
   for row in data.iterrows():
      time = row[1][0]
      passed_circus = row[1][8]
      dict[time] = passed_circus
   return dict


      # pass_roundabout1 = [row1 + row2 for row1, row2 in zip(pass_roundabout, pass_roundabout1[1:])]


if __name__ == "__main__":
   main()

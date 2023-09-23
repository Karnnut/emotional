import pandas as pd
import numpy as np

def main():
   df = pd.read_csv("data.csv")
   # print(df)

   dict_array  = turn_data_into_dict(df)

   for j in dict_array:
      print(dict_array[j])

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
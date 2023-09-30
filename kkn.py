import pandas as pd
import os
import csb

def main():
    directory_aggressive = '/Users/pinto/Desktop/Arbeit/emotional/Aggressive'
    aggressive_time = []
    aggressive_speed_out_list = []
    aggressive_speed_cross_list = []

    for filename in os.scandir(directory_aggressive):
        df = pd.read_csv(filename.path)
        aggressive_time.append(time(df))

        average_speed_out = sum_speed(df)
        average_speed_out1 = average_speed_out[0] / average_speed_out[1]
        aggressive_speed_out_list.append(average_speed_out1)
        
        average_speed_cross = sum_speed_cross(df)
        average_speed_cross1 = average_speed_cross[0] / average_speed_cross[1]
        aggressive_speed_cross_list.append(average_speed_cross1)

    # print(aggressive_speed_cross_list)
    # print(aggressive_speed_out_list)
    # print(aggressive_time)

    directory_cautious= '/Users/pinto/Desktop/Arbeit/emotional/Cautious'
    cautious_time = []
    cautious_speed_out_list = []
    cautious_speed_cross_list = []
    for filename in os.scandir(directory_cautious):
        df = pd.read_csv(filename.path)
        cautious_time.append(time(df))

        average_speed_out = sum_speed(df)
        average_speed_out1 = average_speed_out[0] / average_speed_out[1]
        cautious_speed_out_list.append(average_speed_out1)

        average_speed_cross = sum_speed_cross(df)
        average_speed_cross1 = average_speed_cross[0] / average_speed_cross[1]
        cautious_speed_cross_list.append(average_speed_cross1)

    # print(cautious_speed_cross_list)
    # print(cautious_speed_out_list)
    # print(cautious_time)

    directory_calmly= '/Users/pinto/Desktop/Arbeit/emotional/Calmly'
    calmly_time = []
    calmly_speed_out_list = []
    calmly_speed_cross_list = []
    for filename in os.scandir(directory_calmly):
        df = pd.read_csv(filename.path)
        calmly_time.append(time(df))

        average_speed_out = sum_speed(df)
        average_speed_out1 = average_speed_out[0] / average_speed_out[1]
        calmly_speed_out_list.append(average_speed_out1)

        average_speed_cross = sum_speed_cross(df)
        average_speed_cross1 = average_speed_cross[0] / average_speed_cross[1]
        calmly_speed_cross_list.append(average_speed_cross1)

    # print(calmly_speed_cross_list)
    # print(calmly_speed_out_list)
    # print(calmly_time)

    average_aggressive = find_average(aggressive_time)
    average_cautious = find_average(cautious_time)
    average_calmly = find_average(calmly_time)

    average_speed_out_aggressive = find_average(aggressive_speed_out_list)
    average_speed_out_cautious = find_average(cautious_speed_out_list)
    average_speed_out_calmly = find_average(calmly_speed_out_list)


    average_speed_cross_aggressive = find_average(aggressive_speed_cross_list)
    average_speed_cross_cautious = find_average(cautious_speed_cross_list)
    average_speed_cross_calmly =  find_average(calmly_speed_cross_list)

    print("Average aggressive time:",average_aggressive)
    print("Average cautious time:",average_cautious)
    print("Average calmly time:",average_calmly)

    print("Avera Speed out Aggressive", average_speed_out_aggressive)
    print("Avera Speed out Cautious", average_speed_out_cautious)
    print("Average Speed out Calmly", average_speed_out_calmly)


    print("Average Speed cross Aggressive", average_speed_cross_aggressive)
    print("Average Speed cross Cautious", average_speed_cross_cautious)
    print("Average Speed cross Calmly", average_speed_cross_calmly)


    #---------------------------------------------------------------- Start a Speed Checker --------------------------------

def find_average(list_a):
    count = len(list_a)
    sum = 0
    for i in list_a:
        sum += i
    return sum / count


def time(df):
    last_row = df.iloc[-1]
    final_time = last_row["Time"]
    return final_time


def sum_speed(df):
   sum_speed = 0
   count = 0

   for i in range(0, len(df["Speed"])):
      passed_roundabout = df["Circus entry"]
      speed = df["Speed"]
      if (passed_roundabout[i] == 1) or (passed_roundabout[i] == 2) or (passed_roundabout[i] == 3) or (passed_roundabout[i] == 4) or (passed_roundabout[i] == 5) or (passed_roundabout[i] == 6 ) or (passed_roundabout[i] == 7) or (passed_roundabout[i] == 8) or (passed_roundabout[i] == 9) or (passed_roundabout[i] == 10):
         sum_speed += speed[i]
         count += 1
   
   return sum_speed, count


def sum_speed_cross(df):
   sum_speed = 0
   count = 0

   for i in range(0, len(df["Speed"])):
      passed_cross = df["Crosswalk entry"]
      speed = df["Speed"]
      if (passed_cross[i] == 1) or (passed_cross[i] == 2) or (passed_cross[i] == 3) or (passed_cross[i] == 4) or (passed_cross[i] == 5) or (passed_cross[i] == 6):
         sum_speed += speed[i]
         count += 1
   
   return sum_speed, count


if __name__ == '__main__':
    main()
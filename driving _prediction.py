# import pandas as pd
# import numpy as np

def main():
   # df = pd.read_csv("data01.csv")
   # # print(df)

   # average_speed_out = sum_speed(df)

   # average_speed_out1 = average_speed_out[0] / average_speed_out[1]

   # average_speed_all = sum(df["Speed"]) / len(df["Speed"])

   # average_speed_cross = sum_speed_cross(df)

   # average_speed_cross1 = average_speed_cross[0] / average_speed_cross[1]

   # last_row = df.iloc[-1]

   # final_time = last_row["Time"]

   # print(final_time)

   # print(average_speed_all)

   # print(average_speed_out1)

   # print(average_speed_cross1)


   #result = result_and(final_time, average_speed_out1, average_speed_cross1)
   result = result_and(120, 40, 40)
   print("result", result)
   pesonality = personality_detection(result)
   print(pesonality)
# ---------------------------------------------------------------- Start Results --------------------------------

def personality_detection(data):
   if (data <= 0.43):
      result = "Aggressive"
   elif (data  >= 0.67):
      result= "Calmly"
   else:
      result = "Cautious"

   return result

# ---------------------------------------------------------------- Get a Slope ----------------------------------------------------------------

def getSlope(x1, y1, x2, y2):
    #Avoid zero division error of vertical line for shouldered trapmf
    try:
        slope = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        slope = 0
    return slope

def getYIntercept(x1, y1, x2, y2):
    m = getSlope(x1, y1, x2, y2)
    if y1 < y2:
        y = y2
        x = x2
    else:
        y = y1
        x = x1
    return y - m * x

def result_and(final_time, average_speed_out1, average_speed_cross1):
   sum_ = []
   print(final_time)
   print(average_speed_out1)
   print(average_speed_cross1)
   data1 = [time_low(final_time), speed_round_slow(average_speed_out1), speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data1))
   print("Data1", data1)
   data2 = [time_low(final_time) , speed_round_slow(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data2))
   print("Data2", data2)
   data3 = [time_low(final_time) , speed_round_slow(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data3))
   print("Data3", data3)
   data4 = [time_low(final_time) , speed_round_mid(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data4))
   print("Data4", data4)
   data5 = [time_low(final_time) , speed_round_mid(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data5))
   print("Data5", data5)
   data6 = [time_low(final_time) , speed_round_mid(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data6))
   print("Data6", data6)
   data7 = [time_low(final_time) , speed_round_fast(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data7))
   print("Data7", data7)
   data8 = [time_low(final_time) , speed_round_fast(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data8))
   print("Data8", min(data8))
   data9 = [time_low(final_time) , speed_round_fast(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data9))
   print("Data9", data9)
   data10 = [time_mid(final_time) , speed_round_slow(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data10))
   print("Data10", data10)
   data11 = [time_mid(final_time) , speed_round_slow(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   print(time_mid(final_time), speed_round_slow(average_speed_out1), speed_cross_mid(average_speed_cross1))
   sum_.append(min(data11))
   print("Data11", data11)
   data12 = [time_mid(final_time) , speed_round_slow(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data12))
   print("Data12", data12)
   data13 = [time_mid(final_time) , speed_round_mid(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data13))
   print("Data13", data13)
   data14 = [time_mid(final_time) , speed_round_mid(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data14))
   print("Data14", data14)
   data15 = [time_mid(final_time) , speed_round_mid(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data15))
   print("Data15", data15)
   data16 = [time_mid(final_time) , speed_round_fast(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data16))
   print("Data16", data16)
   data17 = [time_mid(final_time) , speed_round_fast(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data17))
   print("Data17", data17)
   data18 = [time_mid(final_time) , speed_round_fast(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data18))
   print("Data18", data18)
   data19 = [time_mid(final_time) , speed_round_slow(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data19))
   print("Data19", data19)
   data20 = [time_mid(final_time) , speed_round_slow(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data20))
   print("Data20", data20)
   data21 = [time_mid(final_time) , speed_round_slow(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data21))
   print("Data21", data21)
   data22 = [time_mid(final_time) , speed_round_mid(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data22))
   print("Data22", data22)
   data23 = [time_mid(final_time) , speed_round_mid(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data23))
   print("Data23", data23)
   data24 = [time_mid(final_time) , speed_round_mid(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data24))
   print("Data24", data24)
   data25 = [time_mid(final_time) , speed_round_fast(average_speed_out1) , speed_cross_slow(average_speed_cross1)]
   sum_.append(min(data25))
   print("Data25", data25)
   data26 = [time_mid(final_time) , speed_round_fast(average_speed_out1) , speed_cross_mid(average_speed_cross1)]
   sum_.append(min(data26))
   print("Data26", data26)
   data27 = [time_mid(final_time) , speed_round_fast(average_speed_out1) , speed_cross_fast(average_speed_cross1)]
   sum_.append(min(data27))

   print(sum_)
   print("Data27", data27)
   result = max(sum_)
   # result = data1 or data2 or data3 or data4 or data5 or data6 or data7 or data8 or data9 or data10 or data11 or data12 or data13 or data14 or data15 or data16 or data17 or data18 or data19 or data20 or data21 or data22 or data23 or data24 or data25 or data26 or data27

   return result

#---------------------------------------------------------------- Start Time Detection --------------------------------
   

def time_low(data):
   points = [-1, 0, 120, 300]
   result = trapmf(data, points)
   return result


def time_mid(data):
   points = [120, 300, 480]
   result = trimf(data, points);
   return result
      
def time_high(data):
   points = [300, 500, 1000]
   result = trimf(data, points);
   return result

# ---------------------------------------------------------------- Start Speed_roundabout ----------------------------------------------------------------

def speed_round_slow(data):
   points = [-1000, 0, 25]
   result = trimf(data, points);
   return result

def speed_round_mid(data):
   points = [15, 25, 35]
   result = trimf(data, points);
   return result



def speed_round_fast(data):
   points = [25, 50, 1000]
   result = trimf(data, points);
   return result

# ---------------------------------------------------------------- Start Speed Cross----------------------------------------------------------------

def speed_cross_slow(data):
   points = [-17, -2, 10, 25]
   result = trapmf(data, points)
   return result      

def speed_cross_mid(data):
   points = [15, 25, 35]
   result = trimf(data, points)
   return result

def speed_cross_fast(data):
   points = [25, 47, 145, 905]
   result = trapmf(data, points)
   return result

def sum_speed(df):
   sum_speed = 0
   count = 0

   for i in range(0, len(df["Speed"])):
      passed_roundabout = df["Passed Circus"]
      speed = df["Speed"]
      if (passed_roundabout[i] == 1.1) or (passed_roundabout[i] == 2.1) or (passed_roundabout[i] == 3.1) or (passed_roundabout[i] == 4.1):
         sum_speed += speed[i]
         count += 1
   
   return sum_speed, count

def sum_speed_cross(df):
   sum_speed = 0
   count = 0

   for i in range(0, len(df["Speed"])):
      passed_roundabout = df["Passed Crosswalk"]
      speed = df["Speed"]
      if (passed_roundabout[i] == 1) or (passed_roundabout[i] == 2) or (passed_roundabout[i] == 3):
         sum_speed += speed[i]
         count += 1
   
   return sum_speed, count

# ---------------------------------------------------------------- Tramf ----------------------------------------------------------------

def trapmf(x, points):
    pointA = points[0]
    pointB = points[1]
    pointC = points[2]
    print("point C", pointC)
    pointD = points[3]
    slopeAB = getSlope(pointA, 0, pointB, 1)
    slopeCD = getSlope(pointC, 1, pointD, 0)
    yInterceptAB = getYIntercept(pointA, 0, pointB, 1)
    yInterceptCD = getYIntercept(pointC, 1, pointD, 0)
    result = 0
    if x > pointA and x < pointB:
        result = slopeAB * x + yInterceptAB
    elif x >= pointB and x <= pointC:
        result = 1
    elif x > pointC and x < pointD:
        result = slopeCD * x + yInterceptCD
    return result

# ---------------------------------------------------------------- Trimf ----------------------------------------------------------------

def trimf(x, points):
    pointA = points[0]
    pointB = points[1]
    pointC = points[2]
    slopeAB = getSlope(pointA, 0, pointB, 1)
    slopeBC = getSlope(pointB, 1, pointC, 0)
    result = 0
    if x >= pointA and x <= pointB:
        result = slopeAB * x + getYIntercept(pointA, 0, pointB, 1)
    elif x >= pointB and x <= pointC:
        result = slopeBC * x + getYIntercept(pointB, 1, pointC, 0)
    return result

if __name__ == "__main__":
   main()
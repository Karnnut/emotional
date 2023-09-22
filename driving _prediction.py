import pandas as pd

def main():
    df = pd.read_csv("data.csv")
    print(df)
    pass_roundabout = []

    row = len(df)
    for i in range(row):
        time = df[i]
        distance = df[i]
        speed = df[i]
        lap = df[i]
        sector = df[i]
        break_time = df[i]
        map_crashed = df[i]
        car_crashed = df[i]
        passed_roundabout = df[i]
        passed_crosswalk = df[i]
        car_overturned = df[i]
        
        pass_roundabout.append(passed_roundabout)
        
    pass_roundabout1 = [row1 + row2 for row1, row2 in zip(pass_roundabout, pass_roundabout1[1:])]
    

if __name__ == "__main__":
    main()





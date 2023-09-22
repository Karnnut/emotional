import pandas as pd
print(pd. __version__)

df = pd.read_csv("data01.csv")

# Print the row at index 2
row = len(df)
for i in range(row):
    Time = df.iloc[i, 0]
    distance = df.iloc[i, 1]
    lap = df.iloc[i, 2]
    speed = df.iloc[i, 3]
    brake_times = df.iloc[i, 4]
    map_crash = df.iloc[i, 5]
    car_crash = df.iloc[i, 6]
    person_crashed = df.iloc[i, 7]
    all_roundabout = df.iloc[i, 8]
    all_crosswalk = df.iloc[i, 9]
    passed_case_roundabout = df.iloc[i, 10]
    passed_case_crosswalk = df.iloc[i, 11]
    car_overturned = df.iloc[i, 12]
    zone_speed = df.iloc[i, 13]
    is_braked = df.iloc[i, 14]
    
    personality = recognize_personality(df.iloc[i])   
    
    def recognize_behavior(row):
    # Aggressive Behavior
        if (speed > 80 or row['Speed_in_roundabout'] > 100 or row['Speed_before_roundabout'] > 90 or 
            row['car_hit_with_car'] > 5 or row['hit_with_map'] > 5 or row['braked_times'] > 20 or 
            row['dont_stop_in_roundabout'] > 5 or row['pass_case_crosswalk'] < 2 or row['car_overturned'] > 0):
            return "Aggressive"
            
        elif (speed < 50 or row['Speed_in_roundabout'] < 40 or row['Speed_before_roundabout'] < 45 or 
          row['car_hit_with_car'] == 0 or row['hit_with_map'] == 0 or row['braked_times'] < 5 or 
          row['dont_stop_in_roundabout'] == 0 or row['pass_case_crosswalk'] > 10 or row['car_overturned'] == 0):
            return "Cautious"
    
        # Adventurous Behavior (in between)
        elif (speed > 70 or row['Speed_in_roundabout'] > 80 or row['Speed_before_roundabout'] > 70 or 
              row['car_hit_with_car'] > 2 or row['hit_with_map'] > 2 or row['braked_times'] > 10 or 
              row['dont_stop_in_roundabout'] > 2 or row['pass_case_crosswalk'] > 5 or row['car_overturned'] > 0):
            return "Adventurous"
        
        # Defensive Behavior
        elif (row['distance'] > 50 or row['car_hit_with_car'] == 0 or row['braked_times'] > 0 or 
              row['dont_stop_in_roundabout'] == 0 or row['pass_case_crosswalk'] > 5):
            return "Defensive"
    
    # Reckless Behavior
        elif (speed > 90 or row['Speed_in_roundabout'] > 110 or row['Speed_before_roundabout'] > 100 or 
              row['car_hit_with_car'] > 10 or row['hit_with_map'] > 10 or row['braked_times'] > 30 or 
              row['dont_stop_in_roundabout'] > 10 or row['pass_case_crosswalk'] < 1 or row['car_overturned'] > 1):
            return "Reckless"
    
        # Eco-Friendly Behavior
        elif (speed < 60 or row['Speed_in_roundabout'] < 50 or row['Speed_before_roundabout'] < 55 or
              row['car_hit_with_car'] == 0 or row['hit_with_map'] == 0 or row['braked_times'] < 3 or
              row['dont_stop_in_roundabout'] < 2 or row['pass_case_crosswalk'] > 5 or row['car_overturned'] == 0):
            return "Eco-Friendly"
    
        # Competitive Racing Behavior
        elif (speed > 100 or row['Speed_in_roundabout'] > 120 or row['Speed_before_roundabout'] > 110 or
              row['car_hit_with_car'] < 3 or row['hit_with_map'] < 3 or row['braked_times'] > 5 or
              row['dont_stop_in_roundabout'] < 4 or row['pass_case_crosswalk'] < 3 or row['car_overturned'] == 0):
            return "Competitive Racing"
    
        # Distracted Driving Behavior
        else:
            return "Distracted"
    df['Behavior'] = df.apply(recognize_behavior, axis=1)
    print(df[['Time', 'Speed', 'Speed_in_roundabout', 'Speed_before_roundabout', 'car_hit_with_car', 'hit_with_map', 
          'braked_times', 'dont_stop_in_roundabout', 'pass_case_crosswalk', 'car_overturned', 'Behavior']])
    
    # def recognize_personality(df_row):
    #     # Define personality recognition rules here
    #     # Example rules:
    #     if brake_times < 5 and car_crash > 2:
    #         return "Aggressive"
    #     elif brake_times > 10 and distance > 5000:
    #         return "Cautious"
    #     elif passed_case_roundabout > 5 and speed > 60:
    #         return "Adventurous"
    #     else:
    #         return "Unknown"

    # Apply the personality recognition function to the current row

    # Print the recognized personality for the current row
    # print("Personality:", personality)

    # print(Time, distance, lap, speed, brake_times, map_crash, car_crash, person_crashed, all_roundabout, all_crosswalk, passed_case_roundabout, passed_case_crosswalk, car_overturned, zone_speed, is_braked)

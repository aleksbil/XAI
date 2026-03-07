#
def calculate_delivery_eta(distance, average_speed, is_stormy):
    base_time = distance / average_speed

    #explanation
    if is_stormy:
        penalty_ratio = 0.2
        penalty_h = base_time * penalty_ratio
        final_time = base_time + penalty_h
        explanation = f"Delayed due to storm (20% penalty applied: +{penalty_h:.2f} h)."
    else:
        final_time = base_time
        explanation = "Standard conditions (no penalty)."
        
    return final_time, explanation


#distance
while True:
    try:
        distance = float(input('How long is the distance (km)?: '))
        if distance > 0: break
        print("Distance must be greater than 0.")
    except ValueError:
        print('Only numeric value is allowed.')

#speed
while True:
    try:
        average_speed = float(input("Average speed (km/h)?: "))
        if average_speed > 0: break
        print("Average speed must be greater than 0.")
    except ValueError:
        print('Only numeric value is allowed.')

#weather
while True:
    stormy_input = input('Is it stormy? (True/False): ').strip().capitalize()
    if stormy_input == 'True':
        is_stormy = True
        break
    elif stormy_input == 'False':
        is_stormy = False
        break
    else:
        print("Please type 'True' or 'False'.")

#result
eta, msg = calculate_delivery_eta(distance, average_speed, is_stormy)

print("-" * 30)
print(f'Expected ETA: {eta:.2f} h')
print(f'Status: {msg}')
print("-" * 30)

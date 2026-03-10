#ETA
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
#fuel cost
def estimate_fuel_cost(distance, consumption_per_100km, fuel_price):
    total_liters = (distance / 100) * consumption_per_100km
    total_cost = total_liters * fuel_price
    
    #mini-explanatory
    if consumption_per_100km > 30:
        efficiency_note = "High fuel consumption! Consider maintenance."
    else:
        efficiency_note = "Fuel consumption is within the eco-friendly range."
        
    return total_cost, efficiency_note
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

#fuel
print("\n--- FUEL ESTIMATOR ---")
try:
    cons = float(input("Avg consumption (L/100km): "))
    price = float(input("Fuel price per liter (PLN): "))

    #distance from ETA
    cost, note = estimate_fuel_cost(distance, cons, price)
    
    fuel_result = f"Total fuel cost: {cost:.2f} PLN ({note})"
except ValueError:
    fuel_result = "Fuel calculation failed due to invalid input."

#report

print("\n" + "=" * 40)
print(f"       LOGISTICS REPORT       ")
print("=" * 40)
print(f"ROUTE DISTANCE: {distance} km")
print(f"EXPECTED ETA:   {eta:.2f} h")
print(f"TIME STATUS:    {msg}")
print("-" * 40)
print(f"FUEL STATUS:    {fuel_result}")
print("=" * 40)

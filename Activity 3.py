def hotel_cost(night):
    return 140*night
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" ==city:
        return 222
    elif "Los Angelos" == city:
        return 475
    
def rental_car_cost(day):
        if day>=7:
            return 40*day-50
        elif day>=3:
            return 40*day-20
        else:
            return 40*day
def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money

print("The cost of rental car is",rental_car_cost(5))
print("The cost of plane ride is", plane_ride_cost("Los Angelos"))
print("The cost of hotal rooom is", hotel_cost(7))
print("The total cost of trip is", trip_cost("Los Angelos", 7,500))

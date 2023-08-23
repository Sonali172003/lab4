flight_table = {
    "AI161E90": ["BLR", "BOM", 5600],
    "BR161F91": ["BOM", "BBI", 6750],
    "AI161F99": ["BBI", "BLR", 8210],
    "VS171E20": ["JLR", "BBI", 5500],
    "AS171G30": ["HYD", "JLR", 4400],
    "AI131F49": ["HYD", "BOM", 3499]
}

city_codes = {"BLR": "Bengaluru", "BOM": "Mumbai", "BBI": "Bhubaneswar", "HYD": "Hyderabad", "JLR": "Jabalpur"}

def search_flight(param):
    if param == 1:
        city = input("Enter city name: ").upper()
        for k, v in flight_table.items():
            if city in v:
                print(f"Flight ID: {k} From: {city_codes[v[0]]} To: {city_codes[v[1]]} Price: {v[2]}")
    elif param == 2:
        city = input("Enter city name: ").upper()
        for k, v in flight_table.items():
            if city == v[0]:
                print(f"Flight ID: {k} From: {city_codes[v[0]]} To: {city_codes[v[1]]} Price: {v[2]}")
    elif param == 3:
        city1 = input("Enter source city name: ").upper()
        city2 = input("Enter destination city name: ").upper()
        for k, v in flight_table.items():
            if city1 == v[0] and city2 == v[1]:
                print(f"Flight ID: {k} From: {city_codes[v[0]]} To: {city_codes[v[1]]} Price: {v[2]}")

print("Search for Flights:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")

choice = int(input("Enter your choice: "))
search_flight(choice)
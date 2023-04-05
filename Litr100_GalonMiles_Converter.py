def liters_100km_to_miles_gallon(liters):
    miles = 100/1.609344
    gallons = liters/3.785411784
    m_per_gallon = miles/gallons
    return m_per_gallon

def miles_gallon_to_liters_100km(miles):
    kilometrs = 1.609344 * miles
    liters =  3.785411784
    liters_per_100km = (liters/kilometrs)*100
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
miles_int = input('enter integer part of miles ')
miles_fract = input('enter fractional part of miles ')
miles_total = float(miles_int + "." + miles_fract)
km = 1.61 * miles_total
print(f'{miles_total} miles = {km:.1f} km')
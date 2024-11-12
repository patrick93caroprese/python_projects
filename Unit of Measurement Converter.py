#Start building Converter's logic

while True:

    convert_from = input("Enter starting unit of measurement (inches, feet, yards): ")

    convert_to = input("Enter unit of measurement to convert to (inches, feet, yards): ")

    if convert_from.lower() in ["inches", "inch", "in", "i"]:
        number_of_inches = float(input("Enter starting measurement in inches: "))
        if convert_to.lower() in ["feet", "foot", "ft", "f"]:
            print(str(number_of_inches) + " inch = " + str(round(number_of_inches / 12, 2)) + " ft")
        elif convert_to.lower() in ["yards", "yard", "yrds", "yrd", "yds", "yd", "y"]:
            print(str(number_of_inches) + " inch = " + str(round(number_of_inches / 36, 2)) + " yds")
        else:
            print("Your input is incorrect. Please type either inches, yards or feet")

    elif convert_from.lower() in ["feet", "foot", "ft", "f"]:
        number_of_feet = float(input("Enter starting measurement in feet: "))
        if convert_to.lower() in ["inches", "inch", "in", "i"]:
            print(str(number_of_feet) + " ft = " + str(round(number_of_feet * 12, 2)) + " inch")
        elif convert_to.lower() in ["yards", "yard", "yrds", "yrd", "yds", "yd", "y"]:
            print(str(number_of_feet) + " ft = " + str(round(number_of_feet / 3, 2)) + " yds")
        else:
            print("Your input is incorrect. Please type either inches, yards or feet")

    elif convert_from.lower() in ["yards", "yard", "yrds", "yrd", "yds", "yd", "y"]:
        number_of_yards = float(input("Enter starting measurement in yards: "))
        if convert_to.lower() in ["inches", "inch", "in", "i"]:
            print(str(number_of_yards) + " yds = " + str(round(number_of_yards * 36, 2)) + " inch" )
        elif convert_to.lower() in ["feet", "foot", "ft", "f"]:
            print(str(number_of_yards) + " yds = " + str(round(number_of_yards * 3, 2)) + " ft" )
        else:
            print("Your input is incorrect. Please type either inches, yards or feet")

    #Logic in case of a typo
    else:
        print("Your input is incorrect. Please type inches, yards or feet")

    #Logic for another attempt
    next_conversion = input("Wanna do another conversion?? (yes / no): ")

    #Logic for breaking the while loop
    if next_conversion.lower() in ("n", "no", "nope", "no way", "no thanks"):
        break
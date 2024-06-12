from math import log10

# solar constants
mVSun = 4.83 # absolute magnitude
tSun = 5772 # nominal effective temperature, Kelvin
lSun = 3.0128 # luminosity, Watts

def l_tEff(temperature, luminosity):
    return ((tSun/temperature)**4 * luminosity)**0.5

def AD(distance, angular_diameter):
    return distance * angular_diameter/1000 * 107.5

print()
print('Xterminal1 : Stellar Calculator')

while 1:
    calcs = [
        'Radius'
    ]
    for count, ele in enumerate(calcs, 1):
        print(count, ele)
    print()
    calc = int(input('>>> '))

    match calc:
        # Radius
        case 1:
            radius_calcs = [
                'Luminosity-effective temperature', 'Distance-angular diameter', 'Parallax-angular diameter'
            ]
            for count, ele in enumerate(radius_calcs, 1):
                print(count, ele)
            print()
            radius_calc = int(input('>>> '))

            match radius_calc:
                # Luminosity-effective temperature
                case 1:
                    radius = l_tEff(float(input('Effective temperature (Kelvin): ')), float(input('Luminosity (L☉): ')))
                    print()
                    print(f'Radius (R☉): {radius}')

                # Distance-angular diameter
                case 2:
                    radius = AD(float(input('Distance (parsecs): ')), float(input('Angular diameter (milliarcseconds): ')))
                    print()
                    print(f'Radius (R☉): {radius}')

                # Parallax-angular diameter
                case 3:
                    radius = AD(1/float(input('Parallax (milliarcseconds): '))*1000, float(input('Angular diameter (milliarcseconds): ')))
                    print()
                    print(f'Radius (R☉): {radius}')

            print()

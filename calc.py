import math
from math import log10

# solar constants
M_sun = 4.83 # absolute magnitude
T_sun = 5772 # effective temperature [K]
L_sun = 3.0128 # luminosity [W]

def L_R_Teff(calc: int, radius, temp, lum):
    if calc == 1:
        return ((T_sun/temp)**4 * lum)**0.5
    elif calc == 2:
        return (radius/((T_sun/temp)**2))**2
    elif calc == 3:
        return T_sun/(radius/lum**0.5)**0.5
    else:
        return 'ERROR!!!'

def AD(dist, angular_diameter):
    return dist * angular_diameter/1000 * 107.5

def log(param):
    return log10(param/1)

while 1:
    print('-----------------------------------------------------------')
    print('       Xterminal1 : Stellar characteristics calculator')
    print('-----------------------------------------------------------')

    calcs = [
        'Radius', 'Luminosity'
    ]
    for count, ele in enumerate(calcs, 1):
        print(count, ele)
    print()
    calc = input('>>> ')
    if calc.lower() == 'exit':
        print('EXITING...')
        break

    match int(calc):

        # Radius
        case 1:
            radius_calcs = [
                'Luminosity-effective temperature', 'Distance-angular diameter', 'Parallax-angular diameter', 'log(R/R☉)'
            ]
            for count, ele in enumerate(radius_calcs, 1):
                print(count, ele)
            print()
            radius_calc = int(input('>>> '))

            match radius_calc:
                # Luminosity-effective temperature
                case 1:
                    radius = L_R_Teff(1, 0, float(input('Effective temperature [K]: ')), float(input('Luminosity [L☉]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # Distance-angular diameter
                case 2:
                    radius = AD(float(input('Distance [pc]: ')), float(input('Angular diameter [mas]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # Parallax-angular diameter
                case 3:
                    radius = AD(1/float(input('Parallax [mas]: '))*1000, float(input('Angular diameter [mas]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # log(R/R☉)
                case 4:
                    log_radius = log(float(input('Radius [R☉]: ')))
                    print()
                    print(f'log(R/R☉): {log_radius}')

            print()

        # Luminosity
        case 2:
            lum_calcs = [
                'Radius-effective temperature', 'log(L/L☉)'
            ]
            for count, ele in enumerate(lum_calcs, 1):
                print(count, ele)
            print()
            lum_calc = int(input('>>> '))

            match lum_calc:
                # Radius-effective temperature
                case 1:
                    lum = L_R_Teff(2, float(input('Radius [R☉]: ')), float(input('Effective temperature [K]: ')), 0)
                    print()
                    print(f'Luminosity [L☉]: {lum}')

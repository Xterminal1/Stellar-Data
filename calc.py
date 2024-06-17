import math
from math import log10

# solar constants
Mbol_sun = 4.74 # absolute magnitude
Teff_sun = 5772 # effective temperature [K]
L_sun = 3.0128 # luminosity [W]

def LRT(calc: int, radius, Teff, lum):
    if calc == 1:
        return ((Teff_sun/Teff)**4*lum)**0.5
    elif calc == 2:
        return (radius/((Teff_sun/Teff)**2))**2
    elif calc == 3:
        return Teff_sun/(radius/lum**0.5)**0.5
    else:
        return 'ERROR!!!'

def AD(dist, angular_diameter):
    return dist*angular_diameter/1000*107.5

def log(param):
    return log10(param/1)

def L_Mbol(calc: int, lum, Mbol):
    if calc == 1:
        return 10**(0.4*(Mbol_sun-Mbol))
    elif calc == 2:
        return Mbol_sun-2.5*log10(lum)
    else:
        return 'ERROR!'

while 1:
    print('-----------------------------------------------------------')
    print('           Xterminal1 : Stellar data calculator')
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
                    radius = LRT(1, 0, float(input('Effective temperature, Teff [K]: ')), float(input('Luminosity, L [L☉]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # Distance-angular diameter
                case 2:
                    radius = AD(float(input('Distance, d [pc]: ')), float(input('Angular diameter, AD [mas]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # Parallax-angular diameter
                case 3:
                    radius = AD(1/float(input('Parallax, Plx [mas]: '))*1000, float(input('Angular diameter, AD [mas]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # log(R/R☉)
                case 4:
                    log_radius = log(float(input('Radius, R [R☉]: ')))
                    print()
                    print(f'log(R/R☉): {log_radius}')

            print()

        # Luminosity
        case 2:
            lum_calcs = [
                'Radius-effective temperature', 'log(L/L☉)', 'Bolometric magnitude'
            ]
            for count, ele in enumerate(lum_calcs, 1):
                print(count, ele)
            print()
            lum_calc = int(input('>>> '))

            match lum_calc:
                # Radius-effective temperature
                case 1:
                    lum = LRT(2, float(input('Radius, R [R☉]: ')), float(input('Effective temperature, Teff [K]: ')), 0)
                    print()
                    print(f'Luminosity, L [L☉]: {lum}')
                
                # log(L/L☉)
                case 2:
                    log_lum_calcs = ['Calculating luminosity with log(L/L☉)', 'Calculating log(L/L☉) with luminosity']
                    for count, ele in enumerate(log_lum_calcs, 1):
                        print(count, ele)
                    print()
                    log_lum_calc = int(input(">>> "))

                    match log_lum_calc:
                        # Calculating luminosity with log(L/L☉)
                        case 1:
                            pass

                        # Calculating log(L/L☉) with luminosity
                        case 2:
                            log_lum = log(float(input('Luminosity, L [L☉]: ')))
                            print()
                            print(f'log(L/L☉): {log_lum}')
                
                # Mbol
                case 3:
                    Mbol_lum_calcs = ['Calculating luminosity with bolometric magnitude', 'Calculating bolometric magnitude with luminosity']
                    for count, ele in enumerate(Mbol_lum_calcs, 1):
                        print(count, ele)
                    print()
                    Mbol_lum_calc = int(input('>>> '))

                    match Mbol_lum_calc:
                        # Calculating luminosity with bolometric magnitude
                        case 1:
                            lum = L_Mbol(1, 0, float(input('Bolometric magnitude, Mbol: ')))
                            print()
                            print(f'Luminosity, L [L☉]: {lum}')

                        # Calculating bolometric magnitude with luminosity
                        case 2:
                            Mbol = L_Mbol(2, float(input('Luminosity, L [L☉]: ')), 0)
                            print()
                            print(f'Bolometric magnitude, Mbol: {Mbol}')

import math
from math import log10

# solar constants
mBol_sun = 4.74 # absolute magnitude
tEff_sun = 5772 # effective temperature [K]
l_sun = 3.0128 # luminosity [W]

def l_r_tEff(calc: int, r, tEff, l):
    if calc == 1:
        return ((tEff_sun/tEff)**4*l)**0.5
    elif calc == 2:
        return (r/((tEff_sun/tEff)**2))**2
    elif calc == 3:
        return tEff_sun/(r/l**0.5)**0.5
    else:
        return 'ERROR!!!'

def d_theta(d, theta):
    return d*theta/1000*107.5

def log(param):
    return log10(param/1)

def l_mBol(calc: int, l, mBol):
    if calc == 1:
        return 10**(0.4*(mBol_sun-mBol))
    elif calc == 2:
        return mBol_sun-2.5*log10(l)
    else:
        return 'ERROR!'

while 1:
    print('-----------------------------------------------------------')
    print('           Xterminal1 : Stellar data calculator')
    print('-----------------------------------------------------------')

    calcs = [
        'Radius', 'Luminosity', 'Spectral Type'
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
                    radius = l_r_tEff(1, 0, float(input('Effective temperature, Teff [K]: ')), float(input('Luminosity, L [L☉]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # Distance-angular diameter
                case 2:
                    radius = d_theta(float(input('Distance, d [pc]: ')), float(input('Angular diameter, AD [mas]: ')))
                    print()
                    print(f'Radius [R☉]: {radius}')

                # Parallax-angular diameter
                case 3:
                    radius = d_theta(1/float(input('Parallax, Plx [mas]: '))*1000, float(input('Angular diameter, AD [mas]: ')))
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
                'Radius-effective temperature', 'log(L/L☉)', 'Bolometric magnitude', 'Apparent magnitude', 'Absolute magnitude'
            ]
            for count, ele in enumerate(lum_calcs, 1):
                print(count, ele)
            print()
            lum_calc = int(input('>>> '))

            match lum_calc:
                # Radius-effective temperature
                case 1:
                    lum = l_r_tEff(2, float(input('Radius, R [R☉]: ')), float(input('Effective temperature, Teff [K]: ')), 0)
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
                            pass # fix later

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
                            lum = l_mBol(1, 0, float(input('Bolometric magnitude, Mbol: ')))
                            print()
                            print(f'Luminosity, L [L☉]: {lum}')

                        # Calculating bolometric magnitude with luminosity
                        case 2:
                            Mbol = l_mBol(2, float(input('Luminosity, L [L☉]: ')), 0)
                            print()
                            print(f'Bolometric magnitude, Mbol: {Mbol}')

        # Spectral type
        case 3:
            pass




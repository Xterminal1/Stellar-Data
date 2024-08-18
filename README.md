##
# Stellar Data
This repo acts as a database folder for collecting stellar properties for all classes of notable stars, from the smallest red dwarfs to main-sequence stars to the largest known RSGs. 
- calc.py is a Python script that can calculate different properties of a star based on given input parameters and methods. Mass and effective temperature calculators will be added later.

As of 2024, there are two iterations or versions of the collection process.
- Version 1 (1 Apr - 22 Dec 2023)
  - In V1, 447 notable stars, their radii, and spectral classes were listed. Some of the stars listed include white dwarfs, which are technically not considered to be stars.
  - The stellar radii and spectral classes in V1 are from Wikipedia, which is often an inaccurate and inconsistent source. This is improved upon in V2.
  - In V1, many notable RSGs weren't listed, as the primary goal for V1 was to collect radii and spectral classes on regular-sized main-sequence stars.
- Version 2 (ongoing, 5 Jun - )
  - V2 features twice as many notable stars as V1, and it does not include white dwarfs, brown dwarfs, neutron stars, pulsars, magnetars, etc. in the database as they are technically not stars. This is because these objects do not produce energy through nuclear fusion.
  - Most spectral classes for stars in V2 are from SIMBAD. However, if there is a newer and much more accurate spectral class listed in a source on Wikipedia, then it is used instead of SIMBAD's spectral class for the star.
  - The stellar radii for main-sequence stars dimmer than an apparent magnitude (V band) of ~3 come from the Gaia catalogues, specifically DR3 and DR2.
  - Main-sequence stars brighter than ~3 in the V band have their radii derived from accurate sources that were available.
  - The stellar radii for stars above ~300 solar radii come from scientific papers for higher precision.

NOTE: Currently as of 14 June 2024, the focus is on collecting stellar radii on the largest known supergiant and hypergiant stars.

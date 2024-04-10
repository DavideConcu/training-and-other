import numpy as np
import matplotlib.pyplot as plt

# Measured data: wavelength is in millimetres.
measured_lambda=np.array([4.405286344,3.676470588,3.144654088,\
2.754820937,2.450980392,2.004008016,1.834862385,1.377410468,\
0.881834215,0.468823254],float)

# Measured data: intensity in W m**-2 m**-1 sr**-1
measured_intensity=np.array([3.10085E-05,5.53419E-05,8.8836E-05,\
0.000129483,0.000176707,0.000284786,0.00034148,0.000531378,\
0.000561909,6.16936E-05],float)


def blackbody(lamb,T):
    # Planck's constant
    h = 6.62607004E-34
    # Speed of light
    c = 299792458
    # Boltzmann constant
    k = 1.38064852E-23
    # Calculate the blackbody radiation
    intensity = (2*h*c*2/lamb*5)*(1/(np.exp((h*c)/(lamb*k*T))-1))
    return intensity

T = 3000000
bb_intensity = np.array([blackbody(lamb*1E-3,T) for lamb in measured_lambda])
bb_intensity
np.mean(((bb_intensity-measured_intensity)**2)**0.5)


def ROOT_mean_squared_deviation(T):
    # Calculate the blackbody radiation at each wavelength
    bb_intensity = np.array([blackbody(lamb*1E-3,T) for lamb in measured_lambda])
    
    # Calculate the mean squared deviation between the blackbody and measured intensities
    rmsd = np.mean(((bb_intensity-measured_intensity)**2)**0.5)
    return rmsd

# Prompt the user for an initial guess of the temperature
T_guess = float(input("Enter an initial guess for the temperature: "))

# Calculate the mean squared deviation at the initial guess
rmsd = mean_squared_deviation(T_guess)

rmsd

# Keep prompting the user for further guesses until a minimum value is found
while True:
    # Prompt the user for another guess
    T_new = float(input("Enter another guess for the temperature: "))
    # Calculate the mean squared deviation at the new guess
    msd_new = mean_squared_deviation(T_new)
    # If the new value is smaller, update the guess and continue
    if msd_new < msd:
        T_guess = T_new
        msd = msd_new
        continue
    # Otherwise, break out of the loop and report the optimal temperature
    else:
        print("Optimal temperature: {:.4f} K".format(T_guess))
        break

# Create a range of wavelengths to plot the blackbody curve
lamb_range = np.linspace(min(measured_lambda),max(measured_lambda),1000)

# Calculate the blackbody radiation at each wavelength in the range
bb_intensity = np.array([blackbody(lamb*1E-3,T_guess) for lamb in lamb_range])

# Plot the measured data points and the blackbody curve
plt.plot(measured_lambda,measured_intensity,'or',label='Measured')
plt.plot(lamb_range,bb_intensity,label='Blackbody, T={:.4f} K'.format(T_guess))
plt.xlabel('Wavelength (mm)')
plt.ylabel('Intensity (W m$^{-2}$ m$^{-1}$ sr$^{-1}$)')
plt.legend()
plt.show()

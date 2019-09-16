import numpy as np
import matplotlib.pyplot as plt

Y = [1,-1,0,0,0,0,0,0]
Y_K = np.fft.fft(Y)
X_K = np.arange(0,8,1) * np.pi / 4

cont_X_K = np.arange(-4*np.pi,4*np.pi,.01)
cont_Y_K = 1 - np.exp(-cont_X_K*1j)

print(cont_Y_K)

plt.figure()
plt.subplot(121)
plt.scatter(X_K,np.absolute(Y_K),label="Discrete Signal")
plt.plot(cont_X_K,np.absolute(cont_Y_K),c='r',label="Continuous Signal")
plt.title('Exercise 3e) [Module]')
plt.legend(loc='upper right')

#plt.figure()
plt.subplot(122)
plt.scatter(X_K,np.arctan2(Y_K.imag,Y_K.real),label="Discrete Signal")
plt.plot(cont_X_K,np.arctan2(cont_Y_K.imag,cont_Y_K.real),c='r',label="Continuous Signal")
plt.title('Exercise 3e) [Phase]')
plt.legend(loc='upper right')

plt.show()


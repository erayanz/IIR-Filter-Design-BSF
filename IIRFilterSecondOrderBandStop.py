import math
fs= 8000 #Sampling Rate (Hz)
BW=100 #3 dB Bandwidth (Hz)
f0=2000 #center (Hz)
print("fs=",fs,"Hz, 3dB BW=",BW,"Hz, f0=",f0,"Hz")
print("___________________________________________")
#________________________
#Computing r, θ and k:
r=1-(BW*math.pi/fs)
r=float("{:.4f}".format(r))
print("r=",r," , 0.9<=r<1")
theta_degree= (f0/fs)*360
theta=math.radians(theta_degree)
print("θ=",theta_degree,"degree")
k=(1-(2*r*math.cos(theta))+(r**2))/(2-(2*math.cos(theta)))
k=float("{:.4f}".format(k))
print("k=",k,"\n___________________________________________")
#coefficients:
b0=str(k)
b1=k*2*math.cos(theta)
b1=str("{:.4f}".format(b1))
b2=str(k)
a0=str(1)
a1=2*r*math.cos(theta)
#Use 4 digits after comma
a1=str("{:.4f}".format(a1))
a2=r**2
a2=str("{:.4f}".format(a2))
print("Coefficients:")
print("b0=",b0,", b1=",b1,", b2=",b2)
print("a0=",a0,", a1=",a1,", a2=",a2)
#Transfer Function:
#Note: b1=0,a1=0, no z^(-1)
numerator = b0+" + "+b2+"z^(-2)"
denominator = a0+" + "+a2+"z^(-2)"
print("___________________________________________")
print("Transfer Function: ","\n      ",numerator,"\nH(z)= ــــــــــــــــــــــــ","\n       ",denominator)
#Difference Equation:
print("___________________________________________")
print("Difference Equation: ","\ny(n)=",b0+"x(n)+",b2+"x(n-2)-",a2+"y(n-2)")
print("___________________________________________")

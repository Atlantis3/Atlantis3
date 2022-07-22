########## Importing data from the user ############

p = 0.289               # Payload weight
ap = 0.07               # Autopilot weight
ed = 540000             # Energy density of battery
ra = 20000              # Range of UAV
pe = 0.76               # Propeller Effeciency
ldmax= 8                # Maximum Lift to drag ratio
mw = 4.4                # Maximum takeoff weight
a = -0.00296            # coefficient a for empty weight calculation
b = 0.87                # coefficient b for empty weight calculation


#####################################################################
########### CALCULATIONS ############################################


wf=1.05*((9.81*ra)/(pe*ed*ldmax))

we = (a*mw)+b

mwf = (p+ap)/(1-wf-we)
#print(wf)
#print(we)
print ('Your estimated value is ',mw)
print ('The calculated value is ',mwf)

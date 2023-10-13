#Este código recoge toda la mecánica del movimiento rectilíneo uniformemente acelerado con una constante de deceleración de -3m/s.s. Comienza preguntando los datos masa y fuerza para obtener la aceleración necesaria que usaremos 
mass = float(input ("Insert mass in kg of your object:"))
Newtons = float(input ("Insert force applied to your object in newtons:"))
initialaceleration = (Newtons/mass)
kaceleration= -3
print ("your acceleration is:", initialaceleration, "m/s.s")
timeaccelerating = float(input ("Insert amount of time that the force is being applied (in seconds):"))
Initialvelocity = (timeaccelerating*initialaceleration)
print ("your initial velocity is:", Initialvelocity, "m/s")
timetillstop = ((-kaceleration)/Initialvelocity)
print ("It will last you to stop", timetillstop , "seconds")
traveledspace = ((Initialvelocity*timetillstop)-((kaceleration*timetillstop**2)/2))
print ("your object just travelled:", traveledspace, "meters")
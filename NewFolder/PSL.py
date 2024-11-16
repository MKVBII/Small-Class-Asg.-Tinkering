import math 

#Compute the volume of the space in the pan given the radius and depth of said pan 

#input for the radius and height 
pan_radius = int(input('Enter pan radius:'))
pan_height = int(input('Enter pan height:'))

#compute the volume and convert it into fluid ounces 
pan_volume = math.pi*pan_radius*pan_radius*pan_height
panVol_ounces = pan_volume * 0.554

#display the result in fluid ounces
print(f'The volume of the pan in fluid ounces of the spring form pan is {panVol_ounces:.3f} oz')
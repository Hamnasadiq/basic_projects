earth_weight=int(input("Your earth weight: "))
select_planet=str(input("Select planet (MARS,MERCURY,VENUS,JUPYTER,SATURN,URANUS,NEPTUNE): ")).upper()
mars=round((earth_weight*0.378),2)
mercury=round((earth_weight*0.376),2)
venus=round((earth_weight*0.889),2)
jupyter=round((earth_weight*2.36),2)
saturn=round((earth_weight*1.081),2)
uranus=round((earth_weight*0.815),2)
neptune=round((earth_weight*1.14),2)
if select_planet=="MARS":
    print(f"Your weight on MARS is {mars}")
elif select_planet=="MERCURY":
    print(f"Your weight on MERCURY is {mercury}")
elif select_planet=="VENUS":
     print(f"Your weight on VENUS is {venus}")
elif select_planet=="JUPYTER":
    print(f"Your weight on JUPYTER is {jupyter}")
elif select_planet=="SATURN":
    print(f"Your weight on SATURN is {saturn}")
elif select_planet=="URANUS":
     print(f"Your weight on URANUS is {uranus}")
elif select_planet=="NEPTUNE":
     print(f"Your weight on NEPTUNE is {neptune}")
else:
    print("YOU can select only given planets")
import time
now=time.strftime("%d/%m/%Y")
print("It is:",now)

FREEZING_POINT=0
BOILING_POINT=100
def water_state(temperature):
    if temperature <=FREEZING_POINT:
        return"Solid"
    elif FREEZING_POINT<temperature<BOILING_POINT:
        return"Liquid"
    else:
        return"Gas"
print(water_state(-5))
print(water_state(25))
print(water_state(100))

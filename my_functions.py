import random as rnd
#----------------------------------------------------------------------------------------------------------------------------------------+
def fill_list(items:int) -> list: # Get the filled array
    output_list = list()
    counter = 0

    while counter < items:
        output_list.append(rnd.randint(1,50))
        counter += 1
    
    return output_list
#----------------------------------------------------------------------------------------------------------------------------------------+
def fill_list_float_values(items:int) -> list: # Get the filled array
    output_list = list()
    counter = 0

    while counter < items:
        output_list.append(round(rnd.triangular(0.1,50.0),2))
        counter += 1
    
    return output_list
#----------------------------------------------------------------------------------------------------------------------------------------+
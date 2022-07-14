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

#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({order('c') : None})
    new_str = my_string.translate({order('C') : None})
    return new_str

print(no_c("The letter comes nothing"))

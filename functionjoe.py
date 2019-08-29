# Joe Shepherd:its_broken: 9:11 AM
# @channel: Lightning exercise!
# * Write a function that takes a list and a string as args.
# * The string parameter should have a default value.
# * In the function body, loop over the list and print the items, each one prefaced by the value of the string argument
#    * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
# * Try it out! Execute the function both with and without passing in a value for the string parameter

# MUST PUT POSITIONAL PARAMETERS BEFORE ONES WITH DEFAULT VALUES


def takes_list_and_string(cities, stringvalue="I have visited the city of"):
    for city in cities:
        print(f'{stringvalue} {city}')


takes_list_and_string(["San Francisco", "Nashville",
                       "Clarksville"], "I was excited to visit")

takes_list_and_string(["San Francisco", "Nashville", "Clarksville"])

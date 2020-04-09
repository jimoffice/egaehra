from printing_functions import *
from list_operations import *
#1.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#2.

my_list = [12,43]
print(my_list)

sort_list(my_list)
print(my_list)

print(search_by_value(my_list,0))

print(find_five_min_elem(my_list))

print(find_five_max_elem(my_list))

list_avg(my_list)

from decorator import convert_to_strings, convert_to_numbers, pass_by_value


@convert_to_strings
def concat(list_of_items,sep=''):
  return sep.join(list_of_items)
item_list = ["hi", 'there', ".", "i", "am", 29,"years", "old"]
# print(concat(item_list,sep=' '))

@convert_to_numbers
def sum_all(list_of_numbers):
  return sum(list_of_numbers)

list_of_numbers = [1,2,3,43,5,56,4,"3","88"]
# print(sum_all(list_of_numbers))

@pass_by_value
def reverse(list_of_values):
    list_of_values.sort(reverse=True)
    return list_of_values


values_list = [1,2,3,4,5,6,7,8,9]
valuez_list = [2,4,6,8,10]

print(valuez_list )
new_values_list = reverse(valuez_list)
print(new_values_list)
print(valuez_list)




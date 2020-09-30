number_array = [1,2,3,4,5,6,7,8]
len_number_array = int((len(number_array)/2))
total_length = len(number_array) - 1

for iIndex in range(0, len_number_array):
    print(number_array[iIndex], ",", number_array[total_length-iIndex])

sum_all = 0
for single_number in number_array:
    sum_all = sum_all + single_number
print("Sum of all, ", sum_all)

while(True):
    first_input = input("Select 1 to add to list, 2 to delete, 3 to clear, 4 to sort, 5 to exit")
    if first_input == "1":
        print("1")
        second_input = input("Give a number: ")
        if int(second_input) not in number_array:
            number_array.append(int(second_input))
        print(number_array)
    elif first_input == "2":
        second_input = input("Give a number: ")
        if int(second_input) in number_array:
            number_array.remove(int(second_input))
        print(number_array)
    elif first_input == "3":
        number_array.clear()
        print(number_array)
    elif first_input == "4":
        number_array.sort()
        print(number_array)
    elif first_input == "5":
        print("Bye Bye")
        break

#!/usr/bin/python3
# a module that Create a list that contains duplicate values, e.g., [1, 2, 2, 3, 4, 4, 5].

array = [1, 2, 2, 3, 4, 4, 5]


def remove_duplicates(my_list):
    cleaned_list = []
    for num in my_list:
        if num in cleaned_list:
            continue
        else:
            cleaned_list.append(num)
    return cleaned_list, my_list


if __name__  == "__main__":
    result = remove_duplicates(array)
    print(result)


    print(set(array))


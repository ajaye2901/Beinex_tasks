def flatten(lst):

    flatten_list = []

    for i in lst:
        if isinstance(i,list):
            flatten_list.extend(flatten(i))
            print(flatten_list)
        else :
            flatten_list.append(i)
    return flatten_list



lst = [1, [2, 3], [4, [5, 6]]] 
print(flatten(lst))
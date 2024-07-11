def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def main():
    list1 = [[1], [2, 3], [4, 5, 6], []]
    list2 = [['a', 'b'], ['f'], ['g']]
    list3 = [[], [1], [2, 3], [4, 5, 6]]
    list4 = [[], [], []]
    
    print(flatten_list(list1))  
    print(flatten_list(list2))  
    print(flatten_list(list3))  
    print(flatten_list(list4))  

if __name__ == "__main__":
    main()

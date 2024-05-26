def find_majority(items: list):
    print(*items)
    majority_element = items[0]
    count = 1
    for i in range(1,len(items)):
        if items[i] == majority_element:
            count += 1
        else: 
            count -= 1
            if count == 0:
                majority_element = items[i]
                count = 1
    count = 0
    for i in range(len(items)):
        if items[i] == majority_element:
            count += 1

    if count > len(items) // 2:
        print(majority_element )
    else:
        print('Not Found')

find_majority(items = [1, 2, 3, 3, 4, 3, 3, 5 ])
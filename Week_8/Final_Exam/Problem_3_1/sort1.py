def sort1(lst):
    swapFlag = True // swap：交换，flag：标志
    iteration = 0 // 迭代
    while swapFlag: // 
        swapFlag = False
        for i in range(len(lst)-1): 
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        iteration += 1
    return lst

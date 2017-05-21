def f(x):
    '''
    用于计算第x年这1个点的辐射值（可结合速度来理解）
    '''
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposureIteration(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    '''
    用于计算从第start年到第stop年的累计辐射量（可结合速度与时间的成绩=路程来理解）
    step为微积分的精度（可理解为时间）
    '''
    '''
    这里是迭代算法
    '''
    total = 0
    while start < stop:
        total += step * f(start)
        start += step
    return total

print radiationExposureIteration(40, 100, 1.5)
'''
预期输出：0.434612356115
'''

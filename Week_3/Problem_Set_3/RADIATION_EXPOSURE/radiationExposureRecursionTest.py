def f(x):
    '''
    ���ڼ����x����1����ķ���ֵ���ɽ���ٶ�����⣩
    '''
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposureRecursion(start, stop, step):
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
    ���ڼ���ӵ�start�굽��stop����ۼƷ��������ɽ���ٶ���ʱ��ĳɼ�=·������⣩
    stepΪ΢���ֵľ��ȣ������Ϊʱ�䣩
    '''
    '''
    �����ǵݹ��㷨
    '''
    if start - stop >= 0:
        return 0
    return f(start) * step + radiationExposureRecursion(start + step, stop, step)

print radiationExposureRecursion(40, 100, 1.5)
'''
Ԥ�������0.434612356115
'''

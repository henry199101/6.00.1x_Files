def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    # 代码写的有点冗长，目前只能解决s1与s2等长的情形
    s3 = list(s1 + s2)
    s1_index = 0
    s2_index = 0
    s3_index = 0
    while s3_index < len(s3):
          if s3_index % 2 == 0:
                s3[s3_index] = s1[s1_index]
                s1_index += 1
                s3_index += 1
          if s3_index % 2 == 1:
                s3[s3_index] = s2[s2_index]
                s2_index += 1
                s3_index += 1
    return ''.join(s3)

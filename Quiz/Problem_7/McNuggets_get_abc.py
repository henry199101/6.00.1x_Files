def McNuggets_get_abc(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    max_a = n / 6
    max_b = n / 9
    max_c = n / 20
    list_abc = []
    for a in range(max_a + 1):
          for b in range(max_b + 1):
                for c in range(max_c + 1):
                      if 6 * a + 9 * b + 20 * c == n:
                            list_abc.append((a, b, c))
    return list_abc

print McNuggets_get_abc(54)

def pascal_triangle(n):
    """ computes n height Pascal Triangle """
    lis = [1]
    superlis = [[1]]
    if n <= 0:
        return []
    for i in range(n-1):
        prefix = lis.copy()
        for j in range(1, len(lis)):
            prefix[j] = lis[j-1] + lis[j]
        lis = prefix.copy()
        if i + 1 == len(lis):
            lis.append(1)
            superlis.append(lis)
    return superlis

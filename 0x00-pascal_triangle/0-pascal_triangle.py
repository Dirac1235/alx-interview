def pascal_triangle(n):
    lis = [1]
    superlis = [[1]]
    for i in range(n-1):
        prefix = lis.copy()
        
        for j in range(1, len(lis)):
            prefix[j] = lis[j-1] + lis[j]
        lis = prefix.copy()
        if i + 1 == len(lis):
            lis.append(1)
            superlis.append(lis)
    return superlis
        
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

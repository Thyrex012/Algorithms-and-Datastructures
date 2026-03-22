def burrows_wheeler_transform(string: str):
    string += "$"
    BWT = ""

    #Creating the matrix m
    suffixes = []
    for i in range(len(string)):
        suffixes.append(string[i:] + string[:i])
    matrix_m = sorted(suffixes)

    #Getting the BWT
    for suffix in matrix_m:
        BWT += suffix[-1]
        
    return BWT

print(burrows_wheeler_transform("googol"))

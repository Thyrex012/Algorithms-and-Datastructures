def gusfield_z_algorithm(pat, txt):
    str = pat + "$" + txt
    z_array = [-1] * len(str)
    left = 0
    right = 0
    for k in range(1, len(str)):
        if k > right:
            counter = 0
            while counter+k < len(str) and str[counter] == str[counter + k]:
                counter += 1
            z_array[k] = counter
            if z_array[k] > 0:
                left = k
                right = k + z_array[k] - 1
        else:
            #red box is smaller than the green box
            if z_array[k-left] < right - k + 1:
                z_array[k] = z_array[k-left]
            else:
                #red box is equal to or greater than the green
                counter = right - k + 1
                z_array[k] = counter
                while counter+k < len(str) and str[counter] == str[counter + k]:
                    counter += 1
                z_array[k] = counter
                left = k
                right = k + z_array[k] - 1

    final_array = z_array[len(pat)+1:]
    return final_array

def z_algorithm_for_boyer_moore(pat):
    str = pat
    z_array = [-1] * len(str)
    left = 0
    right = 0
    for k in range(1, len(str)):
        if k > right:
            counter = 0
            while counter+k < len(str) and str[counter] == str[counter + k]:
                counter += 1
            z_array[k] = counter
            if z_array[k] > 0:
                left = k
                right = k + z_array[k] - 1
        else:
            #red box is smaller than the green box
            if z_array[k-left] < right - k + 1:
                z_array[k] = z_array[k-left]
            else:
                #red box is equal to or greater than the green
                counter = right - k + 1
                z_array[k] = counter
                while counter+k < len(str) and str[counter] == str[counter + k]:
                    counter += 1
                z_array[k] = counter
                left = k
                right = k + z_array[k] - 1

    return z_array

# pat1 = "sad"
# txt1 = "sadbutsad"
# print(gusfield_z_algorithm(pat1, txt1))

# pat2 = "aaa"
# txt2 = "aaa"
# print(gusfield_z_algorithm(pat2,txt2))
from gusfield_z_algorithm import z_algorithm_for_boyer_moore

def boyer_moore(pat, txt):

    n = len(pat)
    m = len(txt)

    result = []

    #Used for Galil's optimisation
    start = -1
    stop = -1

    #Preprocessing phase
    rx_table = preprocess_bad_char_shift_rule(pat)
    good_suffix = preprocess_good_suffix_rule(pat)
    match_prefix = preprocess_match_prefix_rule(pat)

    # print("good suffx:", good_suffix)
    # print("match prefix:", match_prefix)

    shift = 0

    # comparison = 0

    #Iteration block
    while shift <= m - n:
        # print("current shift is", shift)
        curr_index_pat = n - 1
        while curr_index_pat >= 0 and pat[curr_index_pat] == txt[shift + curr_index_pat]:
            # print(curr_index_pat)
            if curr_index_pat <= stop + 1:
                curr_index_pat = start - 1  # skip the entire window

                #Wrote this to check total number of comparisons
                # comparison += 1
                # print(comparison)

            else:

                curr_index_pat -= 1

                #Wrote this to check total number of comparisons
                # comparison += 1
                # print(comparison)

        # print("stop checking at", curr_index_pat)
        #Mismatch occurs here
        if curr_index_pat >= 0:
            bad_char_shift_amt, start_bad_char, stop_bad_char = bad_char_rule(shift, curr_index_pat, txt, rx_table)
            good_char_shift_amt, start_suffix, stop_suffix = good_suffix_rule(pat, curr_index_pat, good_suffix, match_prefix)
            if good_char_shift_amt >= bad_char_shift_amt:
                start = start_suffix
                stop = stop_suffix
            else:
                start = start_bad_char
                stop = stop_bad_char
            shift += max(bad_char_shift_amt, good_char_shift_amt)
        else:
            # print("pattern has been found starting at index " + str(shift))
            result.append(shift)
            #I have no idea why we'll need to shift by match_prefix[1] NEED TO ASK TEACHER
            shift += n - match_prefix[1]
            start = 0
            stop = match_prefix[1] - 1
    
    return result

#########################
# Preprocessing functions
#########################
def preprocess_bad_char_shift_rule(pat):
    # Creates an Rk(x) table where for each character x, 
    # store the rightmost position of occurances of x in pat to the left of k
    table = []
    prev_row = [-1 for _ in range(26)]
    for i in range(len(pat)):
        table.append(prev_row.copy())
        prev_char_index = ord(pat[i]) - ord('a')
        prev_row[prev_char_index] = i
    return table

def preprocess_good_suffix_rule(pat):

    m = len(pat)
    good_suffix = []

    #Creates a z suffix array so that we can use to determine good suffixes
    rev_pat = pat[::-1]
    z_arr = z_algorithm_for_boyer_moore(rev_pat)
    z_suffix = z_arr[::-1]
    # print("z_sufix:",z_suffix)

    for j in range(m+1):
        good_suffix.append(-1)
    
    for p in range(m - 1):
        j = m - z_suffix[p]
        good_suffix[j] = p
    
    return good_suffix

def preprocess_match_prefix_rule(pat):
    z_arr = z_algorithm_for_boyer_moore(pat)
    m = len(pat)
    match_prefix = [0] * (m+1)
    longest = 0
    for curr_index in range(m-1, -1, -1):
        if curr_index + z_arr[curr_index] - 1 == m - 1:
            longest = z_arr[curr_index]
        match_prefix[curr_index] = longest
    
    #first index should be the entire length of the string itself
    match_prefix[0] = m

    return match_prefix

#########################
#  Iteration functions
#########################
def bad_char_rule(shift, curr_index_pat, txt, rx_table):
    bad_char_index = ord(txt[shift+curr_index_pat]) - ord('a')
    occurance_of_char_in_pat = rx_table[curr_index_pat][bad_char_index]
    start = -1 
    stop = -1
    if occurance_of_char_in_pat != -1:
        return max(1, curr_index_pat - occurance_of_char_in_pat), start, stop
    else:
        return curr_index_pat + 1, start, stop

def good_suffix_rule(pat, index_mismatch, good_suffix, match_prefix):
    m = len(pat)
    if good_suffix[index_mismatch+1] > 0:
        # print("good suffix")
        length_suffix = m - (index_mismatch + 1)
        start = good_suffix[index_mismatch+1] - length_suffix + 1
        stop = good_suffix[index_mismatch+1]
        # print("index of mismatch is", index_mismatch, "start =", start, "stop =", stop)
        return (m-1) - good_suffix[index_mismatch+1], start, stop
    elif good_suffix[index_mismatch+1] == 0:
        # print("match prefix")
        start = 0
        stop = match_prefix[index_mismatch+1] - 1
        # print("index of mismatch is", index_mismatch, "start =", start, "stop =", stop)
        return m - match_prefix[index_mismatch+1], start, stop
    
pat = "abcdeabcdeabcde"
txt = "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde"
# print(preprocess_good_suffix_rule(pat))
print(boyer_moore(pat,txt))
# print(preprocess_match_prefix_rule(pat))
import sys

def check_all_strings_contain_suffix(strings, s, start, end):
    for i in range(len(strings)):
        word = strings[i]
        for j in range(start, end + 1):
            if word[j] != s[j]:
                return False
    return True

def longest_common_prefix(strings):
    min_len = len(min(strings, key=len))
    max_str = max(strings, key=len)
    prefix = ""
    
    low, high = 0, min_len - 1
    while low <= high:
        mid = (low + high)//2
        if check_all_strings_contain_suffix(strings, max_str, low, mid):
            prefix += max_str[low:mid+1]
            low = mid+1
        else:
            high = mid-1
    return prefix

if __name__ == '__main__':
    strings = sys.stdin.readline().strip().split()
    print(longest_common_prefix(strings))




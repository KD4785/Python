# 1. Program to check if array is sorted in ascending using Recursion
def check_sorted(arr, n):
    if n == 1:
        return True
    if arr[0] < arr[1]: 
        return check_sorted(arr[1:], n-1)
    return False

if __name__ == '__main__':
    arr=list(map(int, input("enter array : ").strip().split()))
    n = len(arr)
    print(check_sorted(arr,n))


    

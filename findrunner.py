n = int(input())
arr = set(map(int, input().split()))
arr=list(arr)
arr=sorted(arr,reverse=True)
runner_up=arr[1]
print(runner_up)

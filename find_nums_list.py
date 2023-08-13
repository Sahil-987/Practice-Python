# solution by Amoolya (statsure analystics, Jun/23)
# same solution in GFG website
# Time complexity: O(n^2), where n is the size of the list



a = [1,3,5,7,4,2]
target = 8
list_ans = []
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if a[i] + a[j] == target:
      list_ans.append([a[i],a[j]])

print(list_ans)



"""
alternate solution | GFG website
"""



## technique : Using Sorting and Two Pointers
# Time Complexity:
# The time complexity of this program is O(n log n), 
# where n is the length of the given list. The sorting of the list takes O(n log n) time.
# The two-pointer traversal takes O(n) time. Therefore, 
# the overall time complexity is dominated by the sorting operation.



lst = [1, 5, 3, 7, 9]
K = 12
pairs = []
lst.sort()
left = 0
right = len(lst) - 1

while left < right:
	if lst[left] + lst[right] == K:
		pairs.append((lst[left], lst[right]))
		left += 1
		right -= 1
	elif lst[left] + lst[right] < K:
		left += 1
	else:
		right -= 1

print(pairs)

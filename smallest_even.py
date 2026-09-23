def smallest_even(nums):
  min_even=None
  for num in nums:
    if num%2==0:
      if min_even is None or num<min_even:
        min_even=num
  return min_even
  nums=[2,12,5,4,18,7]
  result=smallest_even(nums)
  print("Smallest even number:",result)

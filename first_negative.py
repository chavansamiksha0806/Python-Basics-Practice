nums=[5,8,12,-3,7,-10]
first_negative=None
for num in nums:
  if num<0:
    first_negative=num
    break
print("First negative number:",first_negative)

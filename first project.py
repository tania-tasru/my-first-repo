# list
country = ["Africa", "India", "Nepal", "Japan", "Indoneshia", "Bangladesh", "America", "China"]
count = len(country)
print(count)

country.pop()
print(country)

print(country[5])
print(country.index("America"))

country.append("Bhutan")
print(country)

country.insert(2, "Maldip")
print(country)

country.remove("India")
print(country)

print("Nepal" in country)
print("Pakisthan" in country)

nums = [2, -7, 0, 45, 78, 98, 3, 66, 100, -1, 8, 10]
print(min(nums))
print(max(nums))

nums.sort()
print(nums)

nums.reverse()
print(nums)

nums1 = nums.copy()  # Copy before clearing
nums.clear()
print(nums)
print(nums1)
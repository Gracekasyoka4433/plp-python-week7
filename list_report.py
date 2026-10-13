# Part C: List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# Print each item with its number
print("SHOPPING LIST REPORT")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# Count item names with more than 4 letters/characters
count = 0
for item in items:
    if len(item) > 4:
        count = count + 1

print("Items with more than 4 letters:", count)

# Find the longest item name using a loop comparison
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)

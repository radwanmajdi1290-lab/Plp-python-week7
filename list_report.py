items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for index in range(len(items)):
    print(f"{index + 1}. {items[index]}")

long_name_count = 0
longest_item = items[0]

for item in items:
    if len(item) > 4:
        long_name_count += 1

    if len(item) > len(longest_item):
        longest_item = item

print("Items with names longer than 4 letters:", long_name_count)
print("Longest item name:", longest_item)

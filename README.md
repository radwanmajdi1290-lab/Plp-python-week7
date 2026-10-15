# Shopping List Manager

- `list_warmup.py` demonstrates list indexing, adding and removing a fruit, and counting list items.
- `shopping_list.py` provides an interactive menu to add, remove, and show shopping-list items.
- `list_report.py` prints a numbered item list, counts long item names, and finds the longest name.

Checking `in` before calling `.remove()` is safer because `.remove()` raises a `ValueError` when the item is not in the list. The membership check lets the program handle that case with a helpful message instead of stopping unexpectedly.

Save a screenshot of each program's output in the `screenshots/` folder before submitting the repository.

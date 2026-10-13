# Week 7 Assignment: Shopping List Manager

## Assignment Overview
This project practices Python list operations, loops, membership checking, and list reporting.

## Files
- `list_warmup.py` — Demonstrates list indexing, adding and removing fruits, and counting list items.
- `shopping_list.py` — Provides a menu-driven shopping list manager to add, remove, display, and manage items safely.
- `list_report.py` — Prints a numbered shopping list, counts item names with more than four characters, and finds the longest item name using a loop.
- `screenshots/` — Contains screenshots showing the output of all three programs.

## Why Check `in` Before Calling `.remove()`?
Checking whether an item is in a list before removing it makes the program safer because `.remove()` raises a `ValueError` when the item does not exist. Using `in` allows the program to display a helpful message instead of stopping with an error. This makes the shopping list manager more reliable and user-friendly.

store1_inventory = {"Laptop","Mouse","Keyboard","Monitor"}
store2_inventory= {"Mouse","Keyboard","Printer","Scanner"}
# Common items in both store
common_items = store1_inventory & store2_inventory
# Items in only store1
only_store1 = store1_inventory - store2_inventory
# Items in only store2
only_store2 = store2_inventory - store1_inventory
# All available items
available_items = store1_inventory | store2_inventory
print("Common items:",common_items)
print("Items in store1:",only_store1)
print("Items in store2:",only_store2)
print("Available items:",available_items)
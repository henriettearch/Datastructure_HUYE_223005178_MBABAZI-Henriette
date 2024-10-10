from collections import deque

# Stack for undoing shipments
undo_stack = []

# Queue for pending shipments
pending_shipments = deque()

# List for tracking inventory
inventory = []
def add_pending_shipment(item):
    pending_shipments.append(item)
    print(f"Added {item} to pending shipments.")
def process_shipment():
    if pending_shipments:
        shipment = pending_shipments.popleft()
        inventory.append(shipment)
        undo_stack.append(shipment)  # Push to undo stack
        print(f"Processed shipment: {shipment}")
    else:
        print("No pending shipments to process.")
def undo_last_shipment():
    if undo_stack:
        last_shipment = undo_stack.pop()
        if last_shipment in inventory:
            inventory.remove(last_shipment)
        print(f"Undone shipment: {last_shipment}")
    else:
        print("No shipments to undo.")
def check_inventory():
    print("Current Inventory:", inventory)
    
    
    


#imprementation /example
# Add shipments to pending queue
#add_pending_shipment("item1")
#add_pending_shipment("item2")
while True:
    product = input("Enter new item or click q to quit/ if you want to undo enter - :\n")
    if(product == 'q'):
        break
    elif(product == '-'):
        # Undo the last shipment
        undo_last_shipment()
        # Check the inventory after undoing
        check_inventory()
    else:
        add_pending_shipment(product)
        process_shipment()
        check_inventory()

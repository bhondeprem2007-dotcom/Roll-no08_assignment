
import gc

class Demo:
    def __init__(self, name):
        self.name = name

obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

print("Garbage collection enabled:", gc.isenabled())

# Create circular reference
obj1.ref = obj2
obj2.ref = obj1

# Delete references
del obj1
del obj2

# Check garbage collection
print("Garbage before collection:", gc.collect())

# Disable automatic garbage collection
gc.disable()
print("Automatic GC disabled:", not gc.isenabled())

# Enable automatic garbage collection
gc.enable()
print("Automatic GC enabled:", gc.isenabled())

print("Garbage collection completed.")

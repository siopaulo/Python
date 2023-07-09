# Create an empty set
s = set()

# Add new elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# set has only unique values so this value won't show up twice
s.add(2)

# Remove value
s.remove(1)

# printing set
print(s)

# printing count of values
print(f"the set has {len(s)} elements.")
def recurse(level:int):
    print(f'recurse {level}')
    if level: # Condition to stop recursion
        recurse(level - 1)
    return


# Test
print(recurse(8))
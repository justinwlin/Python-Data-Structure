'''
Run Time Complexity:

Scenario 1:
for in in range[6]
    print(i)

This runs over the range 6 times.
This would be O(n)

Scenario 2:
for i in range(6)
    for j in range(6)
        print(i)

This runs over it 36 times.
O(n^2)

If it is 3 for-loop it becomes
O(n^3).


Big Oh is Upper Bound
Omega is lower bound
Theta is tight bound, so bounded by top and bottom.
'''
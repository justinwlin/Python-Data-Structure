def appearances(s, low, high):
    if low == high:
        return {s[low]: 1}
    else:
        x = appearances(s, low + 1, high)
        if s[low] in x:
            x[s[low]] += 1
        else:
            x[s[low]] = 1
    return x


print(appearances("testinghaha", 0, 10))
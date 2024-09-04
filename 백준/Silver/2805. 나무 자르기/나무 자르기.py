def get_wood_amount(trees, height):
    return sum(tree - height for tree in trees if tree > height)

def find_max_height(trees, m):
    low, high = 0, max(trees)

    while low <= high:
        mid = (low + high) // 2
        wood = get_wood_amount(trees, mid)

        if wood >= m:
            low = mid + 1
        else:
            high = mid - 1

    return high

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, m))
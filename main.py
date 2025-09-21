# Create a set of visited (0,1)
# In nums find starting position
# Define the bounds len(nums) and len(nums[0])
# Each row has the same number of columns 
# 2 (0,1)

def even_sum(grid, starting_position):
    sum_of_even_nums = 0
    visited = set()

def neighbors(grid, pos):
    r, c = pos
    list_of_neighbors = [
        (r, c-1),
        (r, c+1),
        (r-1, c),
        (r+1, c)
    ]
  
    filtered_list = [ (r,c) for (r,c) in list_of_neighbors if 0 <= r < len(grid) and 0 <= c < len(grid[0]) ]
    
    return filtered_list


nums = (
    (1, 2, 3, 4),
    (7, 8, 6, 4),
    (6, 9, 8, 2),
    (2, 5, 2, 1),
)
assert even_sum(nums, (0, 1)) == 36
assert even_sum(nums, (2, 2)) == 36
assert even_sum(nums, (3, 0)) == 8

print("All tests passed!")
print("Discuss time & space complexity if time remains.")

def even_sum(grid, starting_position):
    # Your code here!
    pass


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

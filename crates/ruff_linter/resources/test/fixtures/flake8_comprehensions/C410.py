l1 = list([1, 2])
l2 = list((1, 2))
l3 = list([])
l4 = list(())


list(  # comment
    [1, 2]
)

list([  # comment
    1, 2
])

# Skip when too many positional arguments
# See https://github.com/astral-sh/ruff/issues/15810
list([1],[2])

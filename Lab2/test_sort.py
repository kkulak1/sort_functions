from sort import bubble_sort, selection_sort, merge_sort, quick_sort


def test_bubble_sort():
    sorted = bubble_sort([4, 3, 7, 11, 3, 6])
    assert sorted == [3, 3, 4, 6, 7, 11]


def test_selection_sort():
    sorted = selection_sort([4, 3, 7, 11, 3, 6])
    assert sorted == [3, 3, 4, 6, 7, 11]


def test_merge_sort():
    sorted = merge_sort([4, 3, 7, 11, 3, 6])
    assert sorted == [3, 3, 4, 6, 7, 11]


def test_quick_sort():
    sorted = quick_sort([4, 3, 7, 11, 3, 6])
    assert sorted == [3, 3, 4, 6, 7, 11]

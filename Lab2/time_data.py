import time
import gc
from sort import bubble_sort, selection_sort, merge_sort, quick_sort


def get_bubble_sort_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        bubble_sort(words_to_measure)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_selection_sort_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        selection_sort(words_to_measure)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_merge_sort_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        merge_sort(words_to_measure)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list


def get_quick_sort_time(words):
    time_list = []
    for i in range(10):
        words_to_measure = words[:(i+1)*1000]

        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        quick_sort(words_to_measure)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        sorting_time = stop - start
        time_list.append(sorting_time)

    return time_list

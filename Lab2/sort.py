import sys
import argparse
import matplotlib.pyplot as plt
import time_data


def open_file(path):
    with open(path, "r") as handle:
        words = read_txt(handle)
    return words


def read_txt(handle):
    words = []
    for line in handle:
        if line.isspace():
            continue
        for word in line.split():
            words.append(word.lower())
    return words


def bubble_sort(words):
    length = len(words)
    for i in range(length - 1):
        for j in range(length - i - 1):
            a = words[j]
            b = words[j+1]
            if words[j] > words[j + 1]:
                words[j] = b
                words[j+1] = a
    return words


def selection_sort(words):
    length = len(words)
    for i in range(length - 1):
        min = i
        for j in range(i+1, length):
            if words[j] < words[min]:
                min = j
        words[i], words[min] = words[min], words[i]
    return words


def merge_sort(words):
    sorted_words = words
    if len(words) > 1:
        middle = len(words)//2
        left = words[:middle]
        right = words[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_words[k] = left[i]
                i += 1
            else:
                sorted_words[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            sorted_words[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            sorted_words[k] = right[j]
            j += 1
            k += 1
    return sorted_words


def quick_sort(words):
    less = []
    equal = []
    greater = []

    if len(words) > 1:
        pivot = words[0]
        for x in words:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return words


def plotter(sort_name, time):
    fig, ax = plt.subplots()
    ax.plot([x * 1000 for x in range(1, 11)],
            time, linewidth=2.0)
    ax.set(xlabel='words(n)', ylabel='time(s)', title=sort_name)
    plt.show()
    # fig.savefig(sort_name, dpi=fig.dpi)


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args(args)
    words = open_file(args.path)
    # print(bubble_sort(words[:1000]))
    # print("--------------------------------")
    # print(selection_sort(words[:1000]))
    # print("--------------------------------")
    # print(merge_sort(words[:1000]))
    # print("--------------------------------")
    # print(quick_sort(words[:1000]))

    data_for_plotter = [("bubble_sort", time_data.get_bubble_sort_time(words)),
                        ("selection sort", time_data.get_selection_sort_time(words)),
                        ("merge sort", time_data.get_merge_sort_time(words)),
                        ("quick sort", time_data.get_quick_sort_time(words))]

    for i in range(4):
        print(data_for_plotter[i][1])
        plotter(data_for_plotter[i][0], data_for_plotter[i][1])


if __name__ == "__main__":
    main(sys.argv[1:])

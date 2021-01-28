# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_faster(numbers: list) -> int:

    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0]*sorted_numbers[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_faster(input_numbers))

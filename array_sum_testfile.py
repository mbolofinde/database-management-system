def array_sum(data):
    """
   list = [1,2,3,4]
   sum = 10
    :param data:
    :return:
    """

    total_sum = 0
    for num in data:
        total_sum += num

    return total_sum


if __name__ == '__main__':
    n = [1, 2, 3, 4]
    rst = array_sum(n)
    print(rst)

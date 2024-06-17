def revers_array(data):
    """
    to reverse an array
    we use 2 pointer method
    we iterate and compare each data and swap thier location
    to rever the list
    e.g. data = "Hello World"
    reversed =  "dlrow olleh"
    :param data:
    :return:
    """
    # lets ensure all in are a list
    data = list(data)

    # let us now define our start and end index references

    first_index_location = 0
    last_index_location = len(data) - 1

    # now we iterate over the list and swap location after comparing

    while first_index_location < last_index_location:
        data[first_index_location], data[last_index_location] = data[last_index_location], data[first_index_location]
        first_index_location += 1
        last_index_location -= 1

    return "".join(data)


if __name__ == '__main__':
    datastr = "hello"
    result = revers_array(datastr)
    print(result)

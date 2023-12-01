def _correct_range(start, stop, step, size):
    # set in case not set (passed None)
    if step is None:
        step = 1
    if start is None:
        if step >= 0:
            start = 0
        else:
            start = size - 1

    if stop is None:
        if step >= 0:
            stop = size
        else:
            stop = -1

    # Check if ranges make sense
    if start >= size:
        if step >= 0:
            start = size
        else:
            start = size - 1
    if start < -size + 1:
        start = -size + 1
    if stop > size:
        stop = size
    if stop < -size:
        if start > 0:
            stop = 0 - 1
        else:
            stop = -size

    if start < 0:
        start = size - start
    if (start > stop and step > 0) or (start < stop and step < 0):
        # swap start and stop
        start, stop = stop, start

    return start, stop, step


def _compute_range(key, shape):
    use_range = any([(index[2] != 1 and index[2]) for index in key])

    range_x = _correct_range(key[-1][0], key[-1][1], key[-1][2], shape[-1])
    range_y = (
        _correct_range(key[-2][0], key[-2][1], key[-2][2], shape[-2])
        if len(shape) > 1
        else [0, 1, 1]
    )
    range_z = (
        _correct_range(key[-3][0], key[-3][1], key[-3][2], shape[-3])
        if len(shape) > 2
        else [0, 1, 1]
    )

    return use_range, range_x, range_y, range_z


def _clean_index(index):
    if not isinstance(index, tuple):
        index = (index,)
    if any(x is Ellipsis for x in index):
        index = tuple(slice(None, None, None) if x is Ellipsis else x for x in index)
    return index

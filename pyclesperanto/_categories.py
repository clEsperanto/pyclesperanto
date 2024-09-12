from inspect import getmembers, isfunction


def categories() -> list:
    """
    Returns a list of all categories of operations in pyclesperanto

    Returns
    -------
    list
        A list of strings with category names
    """

    import pyclesperanto as cle

    ops = getmembers(cle, isfunction)
    cats = {
        cat
        for _, operation in ops
        if hasattr(operation, "categories") and operation.categories is not None
        for cat in operation.categories
    }
    return list(cats)

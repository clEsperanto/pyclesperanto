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

    cats = []

    for _, operation in ops:
        if hasattr(operation, "categories") and operation.categories is not None:
            for cat in operation.categories:
                if cat not in cats:
                    cats = cats + [cat]

    return cats

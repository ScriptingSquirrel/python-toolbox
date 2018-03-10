def touch(path):
    """
    Touches a file at the given `path`.
    Creates the file if it does not yet exist, otherwise only opens and closes the file.
    :param path: The path to the
    :return: None
    """
    with open(path, 'a'):
        pass

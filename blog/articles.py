__author__ = 'lyndon'


class Article:
    """
        Wrapper class for blog.models.Post
    """

    def __init__(self, posts):
        self._posts = posts


class Blog:
    """
        Providing blog interfaces
    """

    def __init__(self): pass
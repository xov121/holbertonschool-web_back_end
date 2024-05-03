#!/usr/bin/env python3
"""A helper function for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index.

    Args:
        page (int): The current page.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

#!/usr/bin/env python3
"""A module for simple pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters"""

    offset = (page - 1) * page_size
    range = [offset, offset + page_size]
    return tuple(range)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a paginated page"""

        """Check that the values' types are correct"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        """Define needed variables"""
        idx_range = index_range(page, page_size)
        start_index = idx_range[0]
        end_index = idx_range[1]
        data = self.dataset()
        the_page = []

        """Check the range"""
        if start_index < len(data) and \
            end_index <= len(data) and \
                start_index <= end_index:
            the_page = data[start_index:end_index]

        return the_page

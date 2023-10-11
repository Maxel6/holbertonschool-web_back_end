#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination method"""

        whole_data = self.indexed_dataset()
        assert isinstance(index, int) and index >= 0
        assert index < len(whole_data)
        assert isinstance(page_size, int) and page_size > 0

        requested_data = []
        start_index = index
        next_index = index + page_size

        for i in range(start_index, next_index):
            if i in whole_data:
                requested_data.append(whole_data[i])
            else:
                next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": requested_data
        }

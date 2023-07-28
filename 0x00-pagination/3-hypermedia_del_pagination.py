#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        implementing hyper_index
        """
        assert index is None or index >= 0
        assert page_size > 0

        dataset = self.dataset()

        if index is None:
            index = 0
        elif index >= len(dataset):
            return {"index": index, "next_index": index,
                    "page_size": page_size, "data": []}

        # Check if there are any rows deleted before the requested index
        deleted_rows = 0
        for i in range(index):
            if i in self.__indexed_dataset and i not in dataset:
                deleted_rows += 1

        # Adjust the index to skip deleted rows
        adjusted_index = index + deleted_rows

        # Get the data for the current page
        current_page_data = []
        for i in range(adjusted_index, adjusted_index + page_size):
            if i < len(dataset):
                current_page_data.append(dataset[i])

        # Find the next index to query with
        next_index = index + page_size

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": current_page_data,
        }

#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page
and page_size.

The function should return a tuple of size two containing a start index and
an end index corresponding to the range of indexes to return in a list
for those particular pagination parameters

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
import csv
import math
from typing import List, Tuple, Dict, Union, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        raise TypeError("page and page_size must be greater than 0")

    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index


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
        """
        return a list of page data
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        page_index = index_range(page, page_size)
        return_list = self.dataset()
        return return_list[page_index[0]:page_index[1]]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10
                  ) -> Dict[str, Union[int, List[List], Optional[int]]]:
        data = self.get_page(page, page_size)
        returned_page_size = len(data)
        all_data = self.dataset()
        beg_to_currpage = page * page_size
        rem_page = len(all_data) - len(all_data[:beg_to_currpage])
        print(len(all_data))
        print(len(all_data[:beg_to_currpage]))
        print(rem_page)
        next_page = page + 1 if rem_page < len(all_data) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': returned_page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

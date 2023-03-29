#!/usr/bin/env python3
"""0x00. Pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ function named index_range that takes two integer arguments
        page and page_size.
    """
    if page == 1:
        return (0, page_size)

    return ((page-1) * page_size, (page - 1) * page_size + page_size)


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
        """  method named get_page that takes two integer arguments page """
        self.dataset()
        if len(self.__dataset) == 0:
            return[]
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        ind_debut, index_end = index_range(page, page_size)
        return(self.__dataset[ind_debut: index_end])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            function a get_hyper method that takes the same arguments (and
            defaults) as get_page and returns a dictionary containing the
            following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        dic = {}

        dic['page_size'] = page_size
        dic['page'] = page
        dic['data'] = self.get_page(page, page_size)

        _lenset = len(self.__dataset)

        if (page + page_size) < _lenset:
            dic['next_page'] = None
        else:
            dic['next_page'] = page + 1

        if (page - page_size) > 1:
            dic['prev_page'] = page - 1
        else:
            dic['prev_page'] = None

        dic['total_pages'] = math.ceil(_lenset / page_size)

        return dic

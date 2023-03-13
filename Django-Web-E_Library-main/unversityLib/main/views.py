from django.shortcuts import render
from .models import Books
from .models import Keyword
from .models import Author

import os
import fitz
from PIL import Image


def keywords_for_menu_dropdown():
    keywords_from_db = Keyword.objects.all()

    cache_counter, amount_counter = 0, 0
    keywords_block, cache_list = [], []
    for keyword in keywords_from_db:
        cache_list.append(keyword)
        cache_counter += 1
        amount_counter += 1
        if cache_counter == 17:
            keywords_block.append(cache_list.copy())
            cache_list.clear()
            cache_counter = 0
        elif amount_counter == len(keywords_from_db):
            keywords_block.append(cache_list.copy())

    return keywords_block


def authors_for_menu_dropdown():
    authors_from_db = Author.objects.all()

    cache_counter, amount_counter = 0, 0
    authors_block, cache_list = [], []
    for author in authors_from_db:
        cache_list.append(author)
        cache_counter += 1
        amount_counter += 1
        if cache_counter == 17:
            authors_block.append(cache_list.copy())
            cache_list.clear()
            cache_counter = 0
        elif amount_counter == len(authors_from_db):
            authors_block.append(cache_list.copy())

    return authors_block


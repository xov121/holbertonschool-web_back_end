#!/usr/bin/env python3
"""Module to list all documents in a collection"""

from typing import List
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[dict]:
    """Lists all documents in a MongoDB collection"""
    return list(mongo_collection.find())

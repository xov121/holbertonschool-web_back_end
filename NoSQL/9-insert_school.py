#!/usr/bin/env python3
"""Module to insert a new document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection to
        insert the document into.
        **kwargs: The key-value pairs representing the document to insert.

    Returns:
        The ID of the new document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

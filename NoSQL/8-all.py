#!/usr/bin/env python3
"""Module to list all documents in a collection."""


def list_all(mongo_collection: Collection):
    """
    Lists all documents in a MongoDB collection.
    """
    return list(mongo_collection.find())

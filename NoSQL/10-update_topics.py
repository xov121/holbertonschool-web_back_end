#!/usr/bin/env python3
"""Module to update topics of a school document in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection to
        update the document in.
        name (str): The school name to update.
        topics (list): The list of topics approached in the school.
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )

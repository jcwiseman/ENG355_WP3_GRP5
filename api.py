"""@file api.py
@brief Helper functions used by the Flask API routes.

@details Contains small utility functions that are imported into app.py
and called from the route handlers.
"""


def api_func_one(name):
    """@brief Returns the name it is given.

    @param name The name to return (e.g. a course name such as "English 355").
    @return The same value that was passed in as @p name.
    """
    return name

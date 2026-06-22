"""Check that the required third-party libraries are installed."""


def test_required_libraries_are_installed():
    import matplotlib  # noqa: F401
    import numpy  # noqa: F401
    import pandas  # noqa: F401
    import seaborn  # noqa: F401

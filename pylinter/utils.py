import path


def collect_sources(ignore_func):
    top_path = path.Path(".")
    for py_path in top_path.walkfiles("*.py"):
        py_path = py_path.normpath()  # get rid of the leading '.'
        if not ignore_func(py_path):
            yield py_path

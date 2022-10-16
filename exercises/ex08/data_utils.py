"""Dictionary related utility functions."""
__author__ = "730554383"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str} of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(vals: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Displays only the amount of rows of data specified by the int argument."""
    rows: dict[str, list[str]] = {}

    for row in vals:
        nvals: list[str] = []
        i: int = 0
        while i < x and i < len(vals[row]):
            nvals.append(vals[row][i])
            i += 1
        rows[row] = nvals
    return rows


def select(vals: dict[str, list[str]], some: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with only a specific subset of the original columns."""
    cols: dict[str, list[str]] = {}

    for name in some:
        nvals: list[str] = []
        for val in vals[name]:
            nvals.append(val)
        cols[name] = nvals
    return cols


def concat(vals_1: dict[str, list[str]], vals_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column based tables combined."""
    vals: dict[str, list[str]] = {}

    for name in vals_1:
        vals[name] = vals_1[name]
    
    for names in vals_2:
        if names in vals:
            i: int = 0
            while i < len(vals_2[names]):
                vals[names].append(vals_2[names][i])
                i += 1
        else:
            vals[names] = vals_2[names]
    return vals


def count(val: list[str]) -> dict[str, int]:
    """Given a list of strs the function produces a dict where each key is a unique value each time a value is associated with that key."""
    vals: dict[str, int] = {}

    for word in val:
        if word in vals:
            vals[word] += 1
        else:
            vals[word] = 1
    return vals
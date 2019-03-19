"""Data Access Object methods."""


def get_all(table, db):
    """Return all the attributes & entries of a table.

    Args:
        table (str): name of the table to query
        db (records.Database): the DB handler

    Returns:
        list(dict): list of table entries

    """
    return db.query(f'SELECT * FROM {table}').as_dict()


def get_by_id(id, prim_key, table, db):
    """Return all the attributes for the single entry matching the ID.

    Args:
        id (int): id of the element to be returned
        prim_key (str): primary key of the of the table to query
        table (str): name of the table to query
        db (records.Database): the DB handler

    Returns:
        dict: entry with the given ID, empty dict if none found

    """
    result = db.query(f'SELECT * FROM {table} WHERE {prim_key} = {id}')
    records = result.as_dict()

    # we return the first and only item
    return records[0] if len(records) == 1 else {}


def create_single(vals, attrs, prim_key, table, db):
    """Insert a single entry into a given table.

    Args:
        vals (list(str)): list of values to insert. Same order as attrs
        attrs (list(str)): list of attributes to be inserted
        prim_key (str): primary key of the table to insert
        table (str): name of the table to insert to
        db (records.Database): the DB handler

    Returns:
        dict: inserted entry, empty dict if failed to create

    """
    escaped_attrs = ', '.join(attrs)
    escaped_vals = ', '.join(f"'{val}'" for val in vals)
    result = db.query(
        f'INSERT INTO {table}({escaped_attrs}) \
        VALUES({escaped_vals}) RETURNING {prim_key}')

    result.all()
    if len(result) != 1:
        return {}

    id = result[0].get(prim_key)
    return get_by_id(id, prim_key, table, db)


def delete_by_id(id, prim_key, table, db):
    """Delete the record with the given primary key from the table.

    Args:
        id (int): the value of the primary key
        prim_key (str): the name of the primary key
        table (str): the name of the table
        db (records.Database): the DB handler

    Returns:
        bool: wether or not the record existed and was deleted

    """
    try:
        db.query(f'DELETE FROM {table} WHERE {prim_key} = {id}')
    except Exception as ex:
        __handle_exception(ex)
        return False
    return True


def update_single(vals, attrs, id, prim_key, table, db):
    """Update a single entry into a given table.

    Args:
        vals (list(str)): list of values to insert. Same order as attrs
        attrs (list(str)): list of attributes to be inserted
        prim_key (str): primary key of the table to insert
        table (str): name of the table to insert to
        db (records.Database): the DB handler

    Returns:
        dict: inserted entry, empty dict if failed to update

    """
    # TODO  there is a potential error here when inserting integers
    #       because we always ' ' the values
    escaped_vals = ', '.join(
        f"{attr} = '{val}'" for attr, val in zip(attrs, vals))

    try:
        db.query(
            f'UPDATE {table} \
            SET {escaped_vals} WHERE {prim_key} = {id}')
    except Exception as ex:
        __handle_exception(ex)
        return False

    return get_by_id(id, prim_key, table, db)


def __handle_exception(ex):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)

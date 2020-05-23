
# Warnings

The `warnings` module writes warning messages to the `sys.stderr` stream:

    :::python
    import warnings

    warnings.warn("This is a drill!")

The output warning also contains a line number:

    :::bash
    warn.py:3: UserWarning: This is a drill!
      warnings.warn("This is a drill!")

Python has an option to stop with an error as soon as a warning occurs:

    :::bash
    python -W error warnme.py

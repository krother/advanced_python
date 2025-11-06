
# Versioning

There are a couple of approaches for versioning:

### Static versioning

Write the version into the `pyproject.toml` file and that's it.

    [project]
    name = "Pac"
    version = "1.0.0"

This version will be used when creating a release or source dist with uv.

### Dynamic versioning

Use a Python file that contains the version number. The build tool will use the `__version__` variable from the referenced file: 

    [project]
    name = "Pac"
    dynamic = ["version"]

    [tool.hatch.version]
    path = "pac/__about__.py"

### Semantic Versioning

Semantic Versioning adds meaning to a version with three numbers like 3.12.7 (`MAJOR.MINOR.PATCH`). You can use the number to identify incompatible versions. See [semver.org/](https://semver.org/)

The [hatch-semver](https://github.com/fleetingbytes/hatch-semver) tool helps maintaining semantic versions.

### Git Tag
The command `git tag` allows you to label commits in your version history with a specific version number, e.g.:

    git tag 1.2.3

Inspect your tags with

    git tag

or

    git log

To integrate Git Tags in your versioning, you may want to use [hatch-vcs](https://github.com/ofek/hatch-vcs).

### bump-my-version

When using an automatic build system, you may want to count up your version number automatically.
One tool for that purpose is bump-my-version [github.com/callowayproject/bump-my-version](https://github.com/callowayproject/bump-my-version).

### Versioning Data with DVC

see [www.python4data.science/en/latest/productive/dvc/index.html](https://www.python4data.science/en/latest/productive/dvc/index.html)

----

Summarized from [https://python-basics-tutorial.readthedocs.io/en/latest/packs/distribution.html](https://python-basics-tutorial.readthedocs.io/en/latest/packs/distribution.html) by Veit Schiele.

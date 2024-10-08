# sphinx-builder-classes

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/agoose77/sphinx-builder-classes/workflows/CI/badge.svg
[actions-link]:             https://github.com/agoose77/sphinx-builder-classes/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/sphinx-builder-classes
[conda-link]:               https://github.com/conda-forge/sphinx-builder-classes-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/agoose77/sphinx-builder-classes/discussions
[pypi-link]:                https://pypi.org/project/sphinx-builder-classes/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/sphinx-builder-classes
[pypi-version]:             https://img.shields.io/pypi/v/sphinx-builder-classes
[rtd-badge]:                https://readthedocs.org/projects/sphinx-builder-classes/badge/?version=latest
[rtd-link]:                 https://sphinx-builder-classes.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

## Usage

This extension defines two Sphinx configuration options that can be set to hide Sphinx nodes with specific class names, e.g.
```python
sphinx_builder_classes_formats = {
  "html": [
    "no-html", "please-no-html" 
  ]
}
```

```markdown
:::{code-cell}
:class: no-html

1 + 2
:::
```

The `sphinx_builder_classes_formats` controls the mapping of builder _format_ to class names, whilst `sphinx_builder_classes_builders` maps from builder _name_ to class names. 

For use with code-cells, one can also use the `<TAG>` -> `tag_<TAG>` transform performed by MyST-NB to use tags to hide cells instead of their classes.

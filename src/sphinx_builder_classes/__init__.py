"""
Copyright (c) 2024 Angus Hollands. All rights reserved.

sphinx-builder-classes: Sphinx extension to hide content based upon the active builder
"""


from __future__ import annotations

from typing import Any

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.docutils import SphinxTranslator

from ._version import version as __version__

__all__ = ["__version__"]


class HiddenNode(nodes.Element):
    """A node that will not be rendered."""

    def __init__(self, rawsource: str = "", *children: nodes.Node, **attributes: Any):
        super().__init__(rawsource, *children, **attributes)

    @classmethod
    def register(cls, app: Sphinx) -> None:
        app.add_node(
            cls,
            override=True,
            html=(visit_HiddenNode, None),
            latex=(visit_HiddenNode, None),
            textinfo=(visit_HiddenNode, None),
            text=(visit_HiddenNode, None),
            man=(visit_HiddenNode, None),
        )


def visit_HiddenNode(self: SphinxTranslator, node: nodes.Element) -> None:  # noqa: ARG001
    raise nodes.SkipNode


class HideNodesTransform(SphinxPostTransform):
    """Hides nodes with the given classes during rendering."""

    default_priority = 400

    def apply(self, **kwargs: Any) -> None:  # noqa: ARG002
        builder_ignore_classes = self.app.config["builder_ignore_classes"]
        ignore_classes = builder_ignore_classes.get(self.app.builder.name, set())
        for node in self.document.traverse(nodes.Element):
            node_classes = set(node["classes"])
            if node_classes & ignore_classes:
                node.replace_self([HiddenNode()])


DEFAULT_BUILDER_IGNORE_CLASSES = {
    "latex": [
        "dropdown",
        "toggle",
        "margin",
    ]
}


def setup(app: Sphinx) -> None:
    app.connect("builder-inited", setup_transforms)
    app.connect("config-inited", setup_ignore_classes)
    app.add_config_value(
        "builder_ignore_classes", DEFAULT_BUILDER_IGNORE_CLASSES, "env", [dict]
    )


def setup_ignore_classes(app: Sphinx, config: Config) -> None:  # noqa: ARG001
    config["builder_ignore_classes"] = {
        k: set(v) for k, v in config["builder_ignore_classes"].items()
    }


def setup_transforms(app: Sphinx) -> None:
    app.add_post_transform(HideNodesTransform)
    HiddenNode.register(app)

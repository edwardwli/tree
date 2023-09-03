import os
from collections.abc import Iterable

Node = dict[str, "Node"]

T_BEND = "├── "
L_BEND = "└── "
VERT = "│   "
BLANK = "    "


def _insert(node: Node, parts: Iterable[str]) -> None:
    for part in parts:
        if part not in node:
            node[part] = Node()
        node = node[part]


def _dfs(node: Node, lines: list[str], verts: list[bool]) -> None:
    for i, (part, subnode) in enumerate(node.items()):
        line_parts = [VERT if vert else BLANK for vert in verts]
        line_parts.append(L_BEND if i == len(node) - 1 else T_BEND)
        line_parts.append(part)

        lines.append("".join(line_parts))

        verts.append(i != len(node) - 1)
        _dfs(subnode, lines, verts)
        verts.pop()


class Trie:
    root: Node

    def __init__(self) -> None:
        self.root = {}

    def insert(self, path: str) -> None:
        _insert(self.root, path.split(os.sep))

    def to_string(self, *, ascii_only: bool) -> str:
        lines: list[str] = []
        for part, node in self.root.items():
            lines.append(part)
            _dfs(node, lines, [])

        return "\n".join(lines)


def make_trie(paths: str, delim: str) -> Trie:
    trie = Trie()
    for path in paths.split(delim):
        trie.insert(path)

    return trie

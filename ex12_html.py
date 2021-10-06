from __future__ import annotations

import random
from dataclasses import dataclass


def main() -> int:
    html = Element("html", attrs={"lang": "en"})
    body = Element("body")
    html.children.append(body)

    heading = Element("h1", text="My opinion on pets")
    body.children.append(heading)

    paragraph = Element("p")
    body.children.append(paragraph)
    animal = random.choice(["cat", "dog"])
    paragraph.text = f"I like {animal}s."
    if animal == "cat":
        paragraph.attrs["class"] = "meow"
    else:
        paragraph.attrs["class"] = "woof"

    breakpoint()

    # Why is the meow/woof class on <body>, <h1>, *and* <p>??
    print(str(html))

    return 0


ALLOWED_TAGS = frozenset(("html", "body", "h1", "p"))


@dataclass
class Element:
    def __init__(
        self,
        tag: str,
        attrs: dict[str, str] = {},
        text: str = "",
    ) -> None:
        assert tag in ALLOWED_TAGS
        self.tag = tag
        self.attrs = attrs
        self.text = text
        self.children: list[Element] = []

    def __repr__(self) -> str:
        return (
            "<Element("
            + f"{self.tag!r}, "
            + f"attrs={self.attrs!r}, "
            + f"text={self.text!r}, "
            + f"children={self.children!r}"
            + ")>"
        )

    def __str__(self) -> str:
        string = "<"
        string += self.tag
        if self.attrs:
            for name, value in self.attrs.items():
                string += " "
                string += name
                string += "='"
                string += value
                string += "'"
        string += ">"
        if self.text:
            string += "\n"
            string += self.text
            string += "\n"
        for child in self.children:
            string += "\n"
            string += str(child)
            string += "\n"
        string += "</"
        string += self.tag
        string += ">"
        return string


if __name__ == "__main__":
    raise SystemExit(main())

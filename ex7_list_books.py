from __future__ import annotations

from pathlib import Path
from typing import cast, TypedDict

import toml


def main() -> int:
    print("All books")

    for book in load_db()["books"]:
        author = get_author(book["author_id"])
        print("*", book["title"], "by", author["name"])

    return 0


# Types


class AuthorDict(TypedDict):
    id: int
    name: str


class BookDict(TypedDict):
    author_id: int
    title: str


class DBDict(TypedDict):
    authors: list[AuthorDict]
    books: list[BookDict]


# Database


db_path = Path(__file__).parent / "ex7_data.toml"


def load_db() -> DBDict:
    db = toml.loads(db_path.read_text())
    # Assume data has the right type
    return cast(DBDict, db)


def get_author(author_id: int) -> AuthorDict:
    authors = load_db()["authors"]
    return [a for a in authors if a["id"] == author_id][0]


if __name__ == "__main__":
    raise SystemExit(main())

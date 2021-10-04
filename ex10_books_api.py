from __future__ import annotations

from html import escape
from pathlib import Path
from typing import TypedDict, cast

import toml
from debug_toolbar.middleware import DebugToolbarMiddleware
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)
app.add_middleware(DebugToolbarMiddleware)


@app.get("/", response_class=HTMLResponse)
def root() -> str:
    html = "<html><body>"
    html += "<h1>All books</h1>"
    html += "<ul>"

    for book in load_db()["books"]:
        author = get_author(book["author_id"])
        html += "<li>"
        html += escape(book["title"])
        html += " by "
        html += escape(author["name"])
        html += "</li>"

    html += "</ul>"
    html += "</body></html>"

    return html


@app.get("/json")
def json():
    book_data = []
    for book in load_db()["books"]:
        author = get_author(book["author_id"])
        book_data.append({"title": book["title"], "author_name": author["name"]})

    return {"books": book_data}


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

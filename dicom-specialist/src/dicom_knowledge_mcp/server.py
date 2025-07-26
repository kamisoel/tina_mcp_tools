import argparse
from contextlib import asynccontextmanager
from typing import Literal
from duckdb import DuckDBPyConnection
from fastmcp import FastMCP
from pathlib import Path

from .db_utils import init_db, search_top_k, add_embedding_fn
from .keyword_search import (
    find_details,
    find_sop_name,
    find_sop_uid,
    get_ciods,
    get_modules,
    get_attributes,
)

mcp = FastMCP("Dicom Specialist")

conn: DuckDBPyConnection
top_k: int


@asynccontextmanager
async def lifespan(server):
    # Starting server
    yield
    # Clean up DB connection on shutdown
    conn.close()


@mcp.tool
def search_dicom_standard(query: str) -> list[str]:
    """Retrieve knowledge about the dicom standard by searching for a query.

    Args:
        query (str): search query
    """
    return search_top_k(conn, query, top_k)


@mcp.tool
def lookup_attribute(attribute: str, domain: str) -> list[dict]:
    """Find details for a Dicom attribute in a given CIOD domain

    Args:
        attribute (str): a dicom attribute name, e.g. Study Date
        domain (str): a dicom CIOD domain, e.g. MR Image

    Returns:
        list[dict]: a sorted list of best matches
    """
    df = find_details(attribute, domain)
    return df.iloc[:3].to_dict(orient="records")


@mcp.tool
def lookup_sop_name(sop_uid: str) -> str:
    """Returns the name for a given SOP ID

    Args:
        sop_uid (str): A dicom SOP UID
    """
    return find_sop_name(sop_uid)


@mcp.tool
def lookup_sop_uid(name: str) -> list[str]:
    """Search for the SOP UID by a given name

    Args:
        name (str): search name

    Returns:
        list[str]: potential SOP UIDs sorted by relevance
    """
    return find_sop_uid(name)


@mcp.tool
def list_names(
    level: Literal["ciod", "module", "attribute"], filter_by: str = "common"
):
    """Returns the names of all CIOD,  modules or attributes

    Args:
        level (Literal[&quot;ciod&quot;, &quot;module&quot;, &quot;attribute&quot;]):
            Specifies if ciods, modules or attributes are returned
        filter_by (str, optional): Filters the list by a given ciod. Does nothing for level=="ciod".
            Use filter_by=="common" to return the ones used by most ciods.
    """
    if level == "ciod":
        return get_ciods()
    elif level == "module":
        return get_modules(ciod=filter_by)
    else:
        return get_attributes(ciod=filter_by)[:250]


def parse_args():
    parser = argparse.ArgumentParser(
        description="RAG based knowledge retrival for the dicom standard"
    )
    parser.add_argument(
        "--db",
        type=str,
        help="Set path to the embeddings database",
        default=Path(__file__).parent / "dicom_db" / "embeddings.db",
    )
    parser.add_argument(
        "--top_k",
        type=int,
        help="Set the number of returned sentences. Default=10",
        default=10,
    )
    parser.add_argument(
        "--embed_model",
        type=str,
        help="Set the embedding model.",
        default="all-MiniLM-L6-v2",
    )
    parser.add_argument(
        "--embed_dim",
        type=str,
        help="Set the embedding dimension.",
        default=384,
    )

    return parser.parse_args()


def main():
    global conn
    global top_k

    args = parse_args()
    conn = init_db(args.db)
    add_embedding_fn(conn, args.embed_model, args.embed_dim)
    top_k = args.top_k
    mcp.run()


if __name__ == "__main__":
    main()

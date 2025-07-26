import duckdb
from sentence_transformers import SentenceTransformer
from duckdb.typing import VARCHAR
import numpy as np


def init_db(name, embedding_dim=384):
    """
    Initialize the DuckDB connection.

    Connects to the DB, installs the vector similarity extension and
    creates the necessary table if not existing.

    Args:
        name (str): file name for DB or :memory: for in-memory DB
        embedding_dim (int, optional): Dimension size for text embeddings. Defaults to 384 (e.g. all-MiniLM-L6-v2 )
    """
    # 1. Connect to DuckDB (in-memory or file-backed)
    conn = duckdb.connect(name)  # or ':memory:'

    # 2. Install & load the vector similarity extension
    conn.execute("INSTALL vss")
    conn.execute("LOAD vss")

    # 3. Create a table with an ARRAY column for vectors
    conn.execute(f"""
    CREATE TABLE IF NOT EXISTS documents (
        node_id     VARCHAR,
        text        VARCHAR,
        embedding   FLOAT[{embedding_dim}]
    )
    """)
    return conn


def add_embedding_fn(conn, model="all-MiniLM-L6-v2", embedding_dim: int = 384):
    """Add a helper function to the DuckDB connection to

    Args:
        conn: DuckDB connection
        model (str, optional): Name of embedding model on HF. Defaults to "all-MiniLM-L6-v2".
        embedding_dim (int, optional): Dimension size for text embeddings. Defaults to 384.
    """

    def embed(sentence: str) -> np.ndarray:
        return model.encode(sentence)

    if isinstance(model, str):
        model = SentenceTransformer(model)
    conn.create_function("embed", embed, [VARCHAR], f"FLOAT[{embedding_dim}]")


def search_top_k(conn, query, top_k=5):
    """Return top-k matches using vector similarity search."""

    response = conn.execute(
        """
        FROM documents
        SELECT text, array_inner_product(embedding, embed($query)) AS similarity
        ORDER BY similarity DESC
        LIMIT $top_k""",
        {"top_k": top_k, "query": query},
    ).fetchall()
    texts, similarities = zip(*response)
    return texts

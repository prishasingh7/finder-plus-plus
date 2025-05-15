import sqlite3
import time
from pathlib import Path

DB_PATH = Path.home() / ".finder_cache.sqlite"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            result TEXT,
            last_accessed REAL,
            access_count INTEGER DEFAULT 1,
            timestamp REAL
        )
    """)
    return conn

def update_cache(query, result):
    now = time.time()
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT id, access_count FROM cache WHERE query = ? AND result = ?", (query, result))
    row = cur.fetchone()

    if row:
        cur.execute("""
            UPDATE cache SET last_accessed = ?, access_count = ? WHERE id = ?
        """, (now, row[1] + 1, row[0]))
    else:
        cur.execute("""
            INSERT INTO cache (query, result, last_accessed, access_count, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (query, result, now, 1, now))

    conn.commit()
    conn.close()
    enforce_cache_limits()

def check_cache(query):
    """Returns a result if a valid one exists in cache within last 30 days."""
    threshold_time = time.time() - 30 * 86400
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT result FROM cache
        WHERE query = ? AND last_accessed >= ?
        ORDER BY access_count DESC, last_accessed DESC
        LIMIT 1
    """, (query, threshold_time))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def enforce_cache_limits():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM cache")
    count = cur.fetchone()[0]
    if count > 200:
        cur.execute("""
            DELETE FROM cache WHERE id IN (
                SELECT id FROM cache ORDER BY last_accessed ASC LIMIT ?
            )
        """, (count - 200,))
    conn.commit()
    conn.close()

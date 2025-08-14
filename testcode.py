import sqlite3


############################################################


def test_code():
    conn = None
    try:
        conn = sqlite3.connect("wordstats.db")
        print(conn)
        with conn:
            c = conn.cursor()
            c.execute(
            """CREATE TABLE anticheat_table (
                username TEXT PRIMARY KEY,
                mention_cnt INTEGER DEFAULT 0
            );
            """
            )
    except sqlite3.Error as e:
        print("Error executing:", e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    test_code()

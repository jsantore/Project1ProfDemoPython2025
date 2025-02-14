import sqlite3
import DataBase.DBUtils


def createDB(cursor: sqlite3.Cursor):

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS jobs_listings(
    job_id INT PRIMARY KEY,
    created_at TEXT,
    updated_at TEXT,
    job_title TEXT NOT NULL,
    job_description TEXT DEFAULT "",
    seniority TEXT,
    full_time TEXT,
    location TEXT NOT NULL,
    company_name TEXT NOT NULL,
    salary INT DEFAULT 0,
    country TEXT NOT NULL,
    url TEXT NOT NULL,
    applicants_count TEXT);"""
    )


def add_locations_Table(cursor: sqlite3.Cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS city_locations(
    city_name TEXT PRIMARY KEY,
    latitude REAL,
    longitude REAL);
    """
    )


def main():
    conn, cursor = DataBase.DBUtils.open_db("Data/JobsAppDB.sqlite3")
    createDB(cursor)
    add_locations_Table(cursor)
    DataBase.DBUtils.close_db(conn)


if __name__ == "__main__":
    main()

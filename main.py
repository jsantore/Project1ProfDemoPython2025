from DataBase.CreateDB import createDB
from DataBase.DBUtils import open_db, close_db
import processData
from os import path


def main():
    conn, cursor = open_db(path.join("Data", "JobsAppDB.sqlite3"))
    createDB(cursor)
    processData.add_rapid_results_to_db("rapidResults.json", cursor)
    processData.add_rapid_api_job_search2_to_db("rapid_jobs2.json", cursor)
    close_db(conn)

if __name__ == "__main__":
    main()

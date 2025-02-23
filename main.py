from DataBase.CreateDB import createDB
from DataBase.DBUtils import open_db, close_db
import processData
from os import path
import PySide6
import sys
from GUI import JobsWindow




def main():
    conn, cursor = open_db(path.join("Data", "JobsAppDB.sqlite3"))
    # consider removing this since the data is there
    createDB(cursor)
    processData.add_rapid_results_to_db("rapidResults.json", cursor)
    processData.add_rapid_api_job_search2_to_db("rapid_jobs2.json", cursor)
    # end consider removing.
    jobs_data = processData.get_jobs_from_db(cursor)
    close_db(conn)
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)
    jobs_window = JobsWindow.JobsWindow(jobs_data)
    sys.exit(qt_app.exec())


if __name__ == "__main__":
    main()

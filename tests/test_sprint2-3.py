import json
import os
import DataBase.CreateDB
import DataBase.DBUtils
import processData
from GUI.JobsWindow import get_complete_job_data

DB_FILE = "Test.db"
JSON_FILE = "Test.json"
test_data = [  # again if we had discussed fixtures, I would do this in a cleaner manner
    {
        "id": "137d56fc45579232",
        "site": "indeed",
        "job_url_direct": "https://www.indeed.com/viewjob?jk=137d56fc45579232",
        "title": "Workday Finance Integrations Analyst",
        "company": "CommuniCare Health Services",
        "location": "Lewis Center, OH, US",
        "job_type": "fulltime",
        "date_posted": "2024-09-04",
        "salary_source": "direct_data",
        "interval": "yearly",
        "min_amount": "73499.0",
        "max_amount": "93066.0",
        "currency": "USD",
        "is_remote": "True",
        "job_level": "",
        "job_function": "",
        "company_industry": "",
        "listing_type": "",
        "emails": "",
        "description": "Big Long Description",
        "ceo_name": "Stephen L. Rosedale",
    },
    {
        "id": "34fvsdfy6df5676546",
        "site": "inword",
        "job_url_direct": "https://www.sillyurl.com/3456tsgert",
        "title": "Super Duper Dev",
        "company": "Big Tech Inc",
        "location": "Bridgewater MA",
        "job_type": "fulltime",
        "date_posted": "2024-09-04",
        "salary_source": "direct_data",
        "interval": "yearly",
        "min_amount": "70000.0",
        "max_amount": "80000.0",
        "currency": "USD",
        "is_remote": "True",
        "job_level": "",
        "job_function": "",
        "company_industry": "",
        "listing_type": "",
        "emails": "",
        "description": "Looking for new grad who wants to learn on the job and do lots of stuff",
        "ceo_name": "Big Wig BSU Grad",
    },
]


def test_create_DB():
    # first make sure that any previous database files are gone so that we are sure the current test is on a new db
    #   if os.path.exists(DB_FILE):
    #       os.remove(DB_FILE)
    # call the 'function under test'
    conn, cursor = DataBase.DBUtils.open_db(DB_FILE)
    DataBase.CreateDB.createDB(cursor)
    DataBase.DBUtils.close_db(conn)
    # now we are sure whatever is in the DB is brand new so if the right table is in the DB, it is because we put it there
    conn, cursor = DataBase.DBUtils.open_db(DB_FILE)
    result_set = cursor.execute(
        "Select * from sqlite_master where name='jobs_listings';"
    )
    assert len(result_set.fetchall()) == 1


def test_load_job_data():
    # I am relying on the fact that tests are run in order by pytest unless you tell it to try to parallelize
    # so the test above will have run and provide us with a brand new empty database with one table
    make_test_json_file()
    conn, cursor = DataBase.DBUtils.open_db(DB_FILE)
    processData.add_rapid_results_to_db(JSON_FILE, cursor)
    conn.commit()
    # DataBase.DBUtils.close_db(conn)  # we need to force a commit
    # conn, cursor = DataBase.DBUtils.open_db(DB_FILE) # now we can test
    cursor.execute("select count(*) from jobs_listings")
    result = cursor.fetchone()
    assert result[0] == len(
        test_data
    )  # fetch one will return a tuple - the count result tuple has only one item
    cursor.execute("select * from jobs_listings")
    result = cursor.fetchall()
    assert (
        result[-1][3] == test_data[-1]["title"]
    )  # I picked the title as the data item I am assuring is correct
    DataBase.DBUtils.close_db(conn)


def make_test_json_file():
    # if this were a real production solution I would use pytest fixtures, but since we haven't talked about them in
    # the course, I'll do this cheap way instead
    # as before - make sure we begin the test suite clean each time.
    if os.path.exists(JSON_FILE):
        os.remove(JSON_FILE)

    with open(JSON_FILE, "w") as out_file:
        for data in test_data:
            json.dump(data, out_file)
            out_file.write("\n")


def test_get_full_data():
    conn, cursor = DataBase.DBUtils.open_db(DB_FILE)
    jobs_data = processData.get_jobs_from_db(cursor)
    result = get_complete_job_data(jobs_data, "34fvsdfy6df5676546")
    assert result["full_time"] == "fulltime"
    assert result["job_title"] == "Super Duper Dev"
    assert (
        result["salary"]
        == f"{test_data[1].get('min_amount')} - {test_data[1].get('max_amount')}"
    )

import json
import sqlite3


def add_rapid_api_job_search2_to_db(file_name: str, cursor: sqlite3.Cursor):
    insert_statement = """INSERT OR IGNORE INTO jobs_listings
            (job_id, created_at, updated_at, job_title, job_description, seniority, full_time,
            location, company_name, salary, country, url, applicants_count)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    with open(file_name, "r") as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            data = json.loads(line)
            for job in data:
                job_tuple = (
                    job.get("id"),
                    job.get("datePosted"),
                    job.get("datePosted"),
                    job.get("title"),
                    job.get("description"),
                    "NOT PROVIDED",
                    job.get("employmentType"),
                    job.get("location"),
                    job.get("company"),
                    job.get("salaryRange"),
                    "NOT PROVIDED",
                    job.get("jobProviders")[0]["url"],
                    "NOT AVAILABLE",
                )
                cursor.execute(insert_statement, job_tuple)


def add_rapid_results_to_db(file_name: str, cursor: sqlite3.Cursor):
    insert_statement = """INSERT OR IGNORE INTO jobs_listings
                (job_id, created_at, updated_at, job_title, job_description, seniority, full_time,
                location, company_name, salary, country, url, applicants_count)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    with open(file_name, "r") as data_file:
        all_lines = data_file.readlines()
        for job_line in all_lines:
            data = json.loads(job_line)
            job_tuple = (
                data.get("id"),
                data.get("datePosted"),
                data.get("datePosted"),
                data.get("title"),
                data.get("description"),
                data.get("job_level"),
                data.get("job_type"),
                data.get("location"),
                data.get("company"),
                f"{data.get('min_amount')} - {data.get('max_amount')}",
                "US",
                data.get("job_url_direct"),
                "NOT PROVIDED",
            )
            cursor.execute(insert_statement, job_tuple)

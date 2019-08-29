import pandas as pd
import time
import requests
import sqlite3

from pyspark.sql import SparkSession


conn = sqlite3.connect("data/students.db")
c = conn.cursor()
# add 'completed' column to students table for summation of completed test runs
c.execute("""ALTER TABLE students ADD COLUMN completed INT DEFAULT 0 NOT NULL;""")


class data_aggregator:

    students_curr_state = None
    batches_curr_state = None
    test_runs_curr_state = None
    report_curr_state = None

    def get_students(self):
        """
        Gets all student records from SQLite db students table,
        Note that student records are continually appended to the database table,
        Recall this method for most up to date list of students

        :return: df: Spark DataFrame
        """
        c.execute("""select * from students;""")
        df = pd.DataFrame(c.fetchall())  # change this to Spark dataframe
        df.columns = [x[0] for x in c.description]
        return df

    def get_batches(self, api_url):
        """
        > Gets first 100 batches and creates 'batches' table in SQLite db
        > Returns Saprk DF of first 100 batches

        :param api_url: str
        :return: df: Spark DataFrame
        """
        pass

    def stream_batches(self, api_url):
        """
        > Streams incoming baches from REST API based on 'after' (creation date) string param,
        > Appends new batches to `batches_curr_state` variable (Spark DF)
        > Inserts new batches into `batches` table in SQLite db

        :param api_url: str
        :return:
        """
        pass

    def stream_test_runs(self, log_file_path):
        """
        > Gets full list of initial test_runs logs from log file, then yields and streams incoming test_runs
        > Cleans and converts test_runs to pure JSON
        > Appends all test_runs to `test_runs_curr_state` variable (JSON object)
        > Creates test_runs table in SQLite db and inserts all incoming stream records

        :param log_file_path: str
        :return: _json: JSON object
        """
        _json = None
        return _json

    def update_student_records(self, students, test_runs):
        """
        > Updates students DF `completed` column based on current test_runs

        :param students: Spark DataFrame
        :param test_runs: JSON object
        """
        pass

    def generate_curr_report(self, students, batches, test_runs):
        """
        > Joins and aggregates students, batches, and test_runs DataFrames
        > Creates `report` DataFrame for batch student performance analysis

        :param students: Spark DataFrame
        :param batches: Spark DataFrame
        :param test_runs: Spark DataFrame
        :return: report: Spark DataFrame
        """
        report = None
        return report

    def create_report_db_table(self, report):
        """
        > Creates or overwrites `report` table in SQLite db with the current state of report for easy analysis
        :param report: Spark DataFrame
        """
        pass

    def get_report_from_sql_query(self):
        """
        > returns Spark DataFrame from sql query (to SQLite db) for a more complete analysis

        :return: report: Spark DataFrame
        """
        pass


def main():
    pass


if __name__ == "__main__":
    main()








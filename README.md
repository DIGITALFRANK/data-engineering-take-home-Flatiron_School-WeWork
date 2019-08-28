# Flatiron School Data Engineering 

Hello, thanks for your interest in a data engineering role at Flatiron School!

## Objective

Given 3 sources of simulated education data, construct a data pipeline prototype that
showcases your capabilities as a problem solver.

The pipeline should culminate in the creation of a database table that would enable
a data analyst to easily report on the batches with the most students that
have completed at least 3 lessons (definitions found in Data Sources section).

This project is very open ended and many hours could easily be invested implementing a solution. Please limit yourself to no more than 3 hours, good timeboxing is as valuable a skill as any!

## Setup

Install Python 3.7 and the dependencies in `requirements.txt`.

## Scripts

* `bin/generate`: Start the data generator.
* `bin/reset`: Delete all generated data.

## Data Sources

### SQLite Student Database

New student records are continuously generated and written to a [SQLite](https://www.sqlite.org/index.html) database located at `data/students.db`.

### Batch REST API

Batches are groups of students, aka a class or section.

The following endpoint responds with a JSON array of up to 100 batch records ordered by creation date being continuously generated.

`GET localhost:8000/batches`

The endpoint accepts an `after` query string parameter, which will return records
only created after the specified time. The format for the time paramater is: `YYYY-MM-DDTHH:MM:SS.SSS`.

### Test Run Log

Test runs are the result of a student executing the test suite for a given
lesson. New data is continuously appended to `data/test_runs.log` as lines of JSON objects.

A test run is considered to have been "completed" if the left hand side of the "results" field is equal to the right hand side.

## Tips

If you don't want to mess with a database server for this project then
[SQLite](https://www.sqlite.org/index.html) can be a useful option. If you're
interested in seeing it being used with Python you can check it out in `data_generator.py`.
# data-engineering-take-home-Flatiron_School-WeWork

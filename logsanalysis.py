#!/usr/bin/env python
#
# An internal tool to analyze data for a new website

# allows connection to server
import psycopg2

# name the database
DBNAME = "news"


def run_tool():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # executes sql query 1
    c.execute(
        "select articles.title, count(log.path) as views from articles "
        "join log on log.path like concat('%', articles.slug) "
        "group by articles.title, log.path order by views desc limit 3;")
    # stores result as var
    top_articles = c.fetchall()
    # executes sql query 2
    c.execute(
        "select authors.name, count(log.path) as views "
        "from authors join articles on authors.id = articles.author "
        "join log on log.path like concat('%', articles.slug) "
        "group by authors.name "
        "order by views desc;")
    # stores result as var
    top_authors = c.fetchall()
    # executes sql query 3
    c.execute(
        "select time::date as day "
        "from log join total_status on "
        "total_status.day = time::date join error_status on "
        "error_status.day = time::date where "
        "round(100 * error_status.e_count / total_status.t_count, 2) > .01 "
        "group by time::date, error_status.e_count, total_status.t_count;")
    # stores result as var
    bug_days = c.fetchall()
    db.close()
    # print out query results
    print("Top Articles: (title / views)")
    for title, views in top_articles:
        print('{0:10} -- {1:10d}'.format(title, views))
    print("\n")
    print("Top Authors: (name / views)")
    for name, views in top_authors:
        print('{0:22} -- {1:10d}'.format(name, views))
    print("\n")
    print("Buggy Dates: (year-month-day)")
    for day in bug_days:
        print (day)[0]
# executes our method
run_tool()

#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def db_connect():
    """
    Creates and returns a connection to the database defined by DBNAME,
    as well as a cursor for the database.
    Returns:
        db, c - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    return [db, c]


def execute_query(c, stmt):
    """Process database access
    args:
    c - cursor
    stmt - sql query statemenet
    Returns:
        Array of values
    """
    c.execute(stmt)
    values = c.fetchall()
    return values


def db_close(db):
    """
    Closes the database
    args:
    db - a database connection
    """
    db.close


def get_pop_three(c):
    """Return three most popular articles."""
    stmt = """
            SELECT title, COUNT(title) AS artcnt
            FROM sluglog, articles
            WHERE status = '200 OK'
            AND articles.slug = sluglog.slug
            GROUP BY title
            ORDER BY artcnt DESC
            LIMIT 3
    """
    articles = execute_query(c, stmt)
    return articles


def get_pop_authors(c):
    """Return Most popular authors."""
    stmt = """
            SELECT name, COUNT(name) AS authcnt
            FROM sluglog, articles, authors
            WHERE articles.slug = sluglog.slug
            AND authors.id = author
            GROUP BY authors.name
            ORDER BY authcnt DESC
    """
    authors = execute_query(c, stmt)
    return authors


def get_1perc_error(c):
    """Return dates with an error greater than 1% of all requests."""
    stmt = """
            SELECT totdt, badcnt * 1.0 / logcnt AS errors
            FROM dailylogcnt, badsrch
            WHERE srchbaddt = totdt 
            AND badcnt > logcnt * 0.01
            ORDER BY totdt
    """
    errors = execute_query(c, stmt)
    return errors


def print_top_articles(c):
    """Prints the top three articles"""
    articles = get_pop_three(c)
    print("{:40s} {:s}".format("Title", "Views"))
    print("{:-<40} {:-<7}".format("", ""))
    for article in articles:
        print("{:40s} {:s}".format(
            article[0], str("{:,}".format(article[1]).rjust(7))))


def print_top_authors(c):
    """Prints a list of authors ranked by article views."""
    print("\n")
    authors = get_pop_authors(c)
    print("{:30s} {:s}".format("Author", "Views"))
    print("{:-<30} {:-<7}".format("", ""))
    for author in authors:
        print("{:30s} {:s}".format(
            author[0], str("{:,}".format(author[1]).rjust(7))))


def print_errors_over_one(c):
    """Prints out the days where more than 1% of logged access requests were errors."""
    print("\n")
    errors = get_1perc_error(c)
    print("{:30s} {:s}".format("Date", "Errors"))
    print("{:-<30} {:-<6}".format("", ""))
    for error in errors:
        print("{:30s} {:.1%}".format(error[0].strftime("%B %d, %Y"), error[1]))


if __name__ == '__main__':
    db, c = db_connect();
    print_top_articles(c)
    print_top_authors(c)
    print_errors_over_one(c)
    db_close (db)

import sqlite3

db_link = "../database.sqlite"


def create_table():
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS  it_team_vulnerability 
            (
                cve_id    varchar(20),
                cve_desc varchar(100),
                it_team varchar(20),
                is_fixed     integer(1)
            )'''
    cursor.execute(query)
    conn.commit()
    conn.close()


def add_vulnerability(cve_id, cve_desc, it_team, is_fixed):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    query = '''INSERT INTO it_team_vulnerability( cve_id, cve_desc, it_team,is_fixed ) VALUES ( ?,?,?,?)'''
    cursor.execute(query, (cve_id, cve_desc, it_team, is_fixed))
    conn.commit()
    conn.close()


def get_all_vulnerability():
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    query = '''SELECT cve_id, cve_desc, it_team, is_fixed FROM it_team_vulnerability'''
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return all_rows


def get_vulnerability_by_cve_id(cve_id):
    get_all_vulnerability()
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    query = '''SELECT cve_id, cve_desc, it_team, is_fixed FROM it_team_vulnerability WHERE cve_id = ?'''
    cursor.execute(query, [cve_id])
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return all_rows


def update_is_fixed_vulnerability(is_fixed, id):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    query = '''UPDATE it_team_vulnerability SET is_fixed = ? WHERE cve_id= ?'''
    cursor.execute(query, (is_fixed, id))
    conn.commit()
    conn.close()


def delete_vulnerability(cve_id):
    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    query = '''DELETE FROM it_team_vulnerability WHERE cve_id = ?'''
    cursor.execute(query, [cve_id])
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return all_rows

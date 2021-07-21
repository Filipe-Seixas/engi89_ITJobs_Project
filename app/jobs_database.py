import sqlite3


def top_live_jobs():
    # Connect to DB
    con = sqlite3.connect('test_jobs.db')
    cur = con.cursor()

    # Get all table names
    cur.execute('''select * from sqlite_master LIMIT 30;''')
    l = cur.fetchall()
    # Create a list to populate with table names and one for later with rank values
    tbl_name_list = []
    rank_list = []
    live_jobs_list = []
    # Populate table name list
    for sql_type, sql_name, tbl_name, rootpage, sql in l:
        if sql_type == 'table':
            tbl_name_list.append(sql_name)

    # Get the rank from all jobs
    for job_name in tbl_name_list:
        cur.execute(f'SELECT rank, live_jobs FROM "{job_name}"')
        job = cur.fetchall()
        # For each rank, append the said rank to the list
        for rank in job:
            rank_list.append(rank[0])
            live_jobs_list.append(rank[1])

    # Save rank data to csv
    dict_list = {}
    # run job name and job risk for loops both at once
    for jN, jR in zip(tbl_name_list, rank_list):
        # add job name as key and job rank as value
        dict_list[jN] = jR
    with open('job_ranks.csv', 'w') as f:
        for key in dict_list.keys():
            f.write("%s,%s\n" % (key, dict_list[key]))

    # Save live_jobs data to csv
    for jN, jR in zip(tbl_name_list, live_jobs_list):
        # add job name as key and job rank as value
        dict_list[jN] = jR
    with open('live_jobs.csv', 'w') as f:
        for key in dict_list.keys():
            f.write("%s,%s\n" % (key, dict_list[key]))




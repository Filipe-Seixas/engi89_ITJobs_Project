import sqlite3


class Database:

    # Connect to Database
    db = sqlite3.connect('app/test_jobs.db', check_same_thread=False)
    dbc = db.cursor()

    # Create Table
    def database_initialise(self, job_title):
        self.db.execute(f'CREATE TABLE IF NOT EXISTS {job_title} (date DATETIME, rank INTEGER, median_salary DOUBLE, '
                        f'hist_perm_job INTEGER, live_jobs INTEGER)')

    # Populate Tables with data
    def add_jobs(self, job_date, job_title, job_rank, job_median_sal, job_hist_ads, jobs_live):
        self.db.execute(
            f'INSERT INTO {job_title} (date, rank, median_salary, hist_perm_job, live_jobs) VALUES ("{job_date}", '
            f'"{job_rank}", "{job_median_sal}", "{job_hist_ads}", "{jobs_live}")')
        self.db.commit()
        print(f"Python Variables inserted successfully into {job_title} ")

    def top_live_jobs1(self):
        all_jobs = self.get_jobs()
        data = []
        for job in all_jobs:
            self.dbc.execute(f'SELECT live_jobs FROM {job} ORDER BY live_jobs DESC LIMIT 1')
            for i in self.dbc.fetchall():
                data.append((job,i[0]))
        sorted_by_second = sorted(data, key=lambda tup: tup[1], reverse=True)[:30]
        print(sorted_by_second)
        with open('live_jobs.csv', 'w') as f:
            for value in sorted_by_second:
                f.write("%s,%s\n" % value)

    # Get Top 30 jobs by rank and save to csv file
    def top_rank1(self):
        all_jobs = self.get_jobs()
        data = []
        for job in all_jobs:
            self.dbc.execute(f'SELECT rank FROM {job} ORDER BY rank DESC LIMIT 1')
            for i in self.dbc.fetchall():
                data.append((job, i[0]))
        sorted_by_second = sorted(data, key=lambda tup: tup[1])[:30]
        print(sorted_by_second)
        with open('job_ranks.csv', 'w') as f:
            for value in sorted_by_second:
                f.write("%s,%s\n" % value)
        return data

    def all_data(self):
        all_jobs = self.get_jobs()
        data = []
        for job in all_jobs:
            self.dbc.execute(f'SELECT * FROM {job}')
            for i in self.dbc.fetchall():
                data.append((job, i[0]))
        print(data)
        return(data)


    def get_jobs(self):
        jobs_list = []
        self.dbc.execute('''SELECT name
                       FROM sqlite_master
                       ORDER BY name
                    ''')
        for i in self.dbc.fetchall():
            jobs_list.append(i[0])
        return jobs_list


d = Database()
#d.top_live_jobs1()
#d.top_rank1()


import re
import psycopg2

from itemadapter import ItemAdapter


class GamesPipelineCleanAndWrite:
    def open_spider(self, spider):
        user = 'postgres'
        password = 'Pass1213'
        dbname = 'gamesdb'
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        self.cur = self.conn.cursor() 

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id serial PRIMARY KEY, 
            title varchar,
            rating float,
            url varchar,
            alt_name varchar,
            year integer,
            platform varchar,
            released_in varchar,
            genre varchar,
            theme varchar,
            publisher varchar,
            developer varchar, 
            perspectives varchar);
        ''')  
        self.conn.commit()

    def close_cpider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        # clean data
        remover = re.compile(r'<[^>]+>')
        for field in item.keys():
            item[field] = remover.sub('', item[field][0])
            if field == 'rating':
                item[field] = float(item[field])
            if field == 'year':
                item[field] = int(item[field])
        
        # check the duplicates
        self.cur.execute('SELECT * from games WHERE url = %s;', [item['url']])
        result = self.cur.fetchone()
        if not result:
            fields = [field for field in item.keys()]
            values = [item[field] for field in fields]

            insert_query = f"""
                INSERT INTO games ({', '.join(fields)}) 
                VALUES ({', '.join(['%s'] * len(values))});
            """

            self.cur.execute(insert_query, values)
            self.conn.commit()

        return item


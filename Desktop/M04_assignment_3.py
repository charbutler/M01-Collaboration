$pip install sqlalchemy
import create_engine
engine = create_engine('sqlite:///books.db')
connection = engine.connect()
result = connection.execute("SELECT title FROM books ORDER BY title ASC")
for row in result:
    print(row['title'])
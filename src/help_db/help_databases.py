from databases import Database
import asyncio

async def main():
    database = Database('postgresql://postgres:1234@127.0.0.1:5432/db')
    await database.connect()

    # Create a table.
    #query = """CREATE TABLE HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
    #await database.execute(query=query)

    # Insert some data.
    query = "INSERT INTO HighScores(id, name, score) VALUES (:id, :name, :score)"
    values = [
        {"id":1, "name": "Daisy", "score": 92},
        {"id":2, "name": "Neil", "score": 87},
        {"id":3, "name": "Carol", "score": 43},
    ]
   # await database.execute_many(query=query, values=values)

    # Run a database query.
    query = "SELECT * FROM HighScores"
    rows = await database.fetch_all(query=query)
    print('High Scores:', rows)

asyncio.run(main())
import sqlite3

class Todos_sql():
    def __init__(self):
        connect = sqlite3.connect("database/todos.db")
        data = connect.cursor()
        data.execute("""
        -- TODOS table
        CREATE TABLE IF NOT EXISTS TODOS (
           name text NOT NULL,
           description text,
           done integer
        );
        """)
        data.execute("""
            select * from TODOS
            """)
        self.todos = []
        todo_data = data.fetchall()
        for a, b, c in todo_data:
            if c == 1:
                c = True
            else:
                c = False
            dictionary = {"title": a, "description": b, "done": c}
            self.todos.append(dictionary)
        connect.close()


    def all(self):
        return self.todos

    def get(self, id):
        return self.todos[id]

    def create(self, data):
        data.pop('csrf_token')
        self.todos.append(data)

    def save_all(self):
        connect = sqlite3.connect("Database/todos.db")
        data = connect.cursor()
        data.execute("delete from TODOS")
        connect.commit()
        for i in self.all():
            title, description, done = i["title"], i["description"], i["done"]
            if done == True:
                done = 1
            else:
                done = 0
            data.execute(f"""
            INSERT INTO TODOS (name,description,done)
            VALUES('{title}','{description}',{done})
            """)
            connect.commit()
        connect.close()

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

    def delete(self,id):
        del self.todos[id]
        self.save_all()


todos = Todos_sql()
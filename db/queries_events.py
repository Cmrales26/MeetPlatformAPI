from db import connection_postgreSQL

connection = connection_postgreSQL.connection
# Business


def CreateEvent(data):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO public.event("EventID", "Name", "Description", "_BusinessID", "Date", "Hour", "location") VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (
                data["id"],
                data["name"],
                data["description"],
                data["businessID"],
                data["date"],
                data["time"],
                data["location"],
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


# Users

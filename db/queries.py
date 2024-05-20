from db import connection_postgreSQL

connection = connection_postgreSQL.connection


def UserExists(id):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM public."user" WHERE "UserID" = %s', (id,))
        user = cursor.fetchone()
        if user is not None:
            return True
        else:
            return False
        cursor.close()
    except Exception as ex:
        return False


def CheckNormalUser(email):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM public."user" WHERE "Email" = %s', (email,))
        user = cursor.fetchone()
        if user is not None:
            column_names = [desc[0] for desc in cursor.description]
            user_dict = dict(zip(column_names, user))
            user_dict["BirthDate"] = str(user_dict["BirthDate"])
            user_dict["Phone"] = str(user_dict["Phone"])
            if user_dict["Status"] == False:
                return "Disable"
            return user_dict
        else:
            return None
        cursor.close()
    except Exception as ex:
        return False


def CreateNormalUser(data):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO public."user" ("UserID", "Name", "LastName", "Bio", "BirthDate", "Email", "Phone", "Password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (
                data["id"],
                data["name"],
                data["lastname"],
                data["bio"],
                data["birth"],
                data["email"],
                int(data["phone"]),
                data["password"],
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


def UpdateUser(id, data):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE public."user" SET "Name" = %s, "LastName" = %s, "Bio" = %s, "BirthDate" = %s, "Phone" = %s WHERE "UserID" = %s',
            (
                data["name"],
                data["lastname"],
                data["bio"],
                data["birth"],
                int(data["phone"]),
                id,
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


def ChangePassword(email, password):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE public."user" SET "Password" = %s WHERE "Email" = %s',
            (
                password,
                email,
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False

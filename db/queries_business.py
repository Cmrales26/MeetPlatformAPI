from db import connection_postgreSQL
import json

connection = connection_postgreSQL.connection


def BusinessExists(id):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM public.business WHERE "BusinessID" = %s', (id,))
        user = cursor.fetchone()
        if user is not None:
            return True
        else:
            return False
        cursor.close()
    except Exception as ex:
        return False


def CreateBusiness(data):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO public.business ("BusinessID", "Name", "Bio", "FundationDate", "Password") VALUES (%s, %s, %s, %s, %s)',
            (
                data["id"],
                data["name"],
                data["bio"],
                data["fundationdate"],
                data["password"],
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


def CheckBusinessUser(name):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM public.business Where "Name" = %s', (name,))
        user = cursor.fetchone()
        if user is not None:
            column_names = [desc[0] for desc in cursor.description]
            user_dict = dict(zip(column_names, user))
            user_dict["FundationDate"] = str(user_dict["FundationDate"])
            if user_dict["Status"] == False:
                return "Disable"
            return user_dict
        else:
            return None
        cursor.close()
    except Exception as ex:
        return False


def UpdateBusiness(data, id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE public.business SET "Bio" = %s, "FundationDate" = %s WHERE "BusinessID" = %s',
            (data["bio"], data["fundationdate"], id),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


def ChangePasswordB(name, password):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE public."business" SET "Password" = %s WHERE "Name" = %s',
            (
                password,
                name,
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


def DisableBusiness(id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE public.business SET "Status" = False WHERE "BusinessID" = %s',
            (id,),
        )
        connection.commit()
        connection.close()
        return True
    except:
        return False

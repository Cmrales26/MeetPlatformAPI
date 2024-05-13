from db import connection_postgreSQL

connection = connection_postgreSQL.connection

# Business


def Get_Event(BusinessID):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM public.event WHERE "_BusinessID" = %s', (BusinessID,)
        )
        events = cursor.fetchall()

        event_list = []

        if len(events) == 0:
            return event_list

        for event in events:
            event_dict = {
                "id": event[0],
                "name": event[1],
                "description": event[2],
                "businessID": event[3],
                "date": event[4].isoformat(),
                "time": event[5].isoformat(),
                "location": event[6],
            }
            event_list.append(event_dict)
        cursor.close()
        return event_list
    except Exception as ex:
        return False


def Get_Event_by_id(EventID, businessID):
    print(businessID)
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM public.event WHERE "EventID" = %s AND "_BusinessID" = %s',
            (EventID, businessID),
        )
        event = cursor.fetchone()
        if event is not None:
            event_dict = {
                "id": event[0],
                "name": event[1],
                "description": event[2],
                "businessID": event[3],
                "date": event[4].isoformat(),
                "time": event[5].isoformat(),
                "location": event[6],
            }
            return event_dict
        else:
            return None
        cursor.close()
    except Exception as ex:
        return False


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


# Validate Events
def validate_event_permission(BusinessID, EventID):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM public.event WHERE "EventID" = %s AND "_BusinessID" = %s',
            (EventID, BusinessID),
        )
        user = cursor.fetchone()
        if user is not None:
            return True
        else:
            return False
        cursor.close()
    except Exception as ex:
        return False


def update_event(EventId, data):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE public.event SET "Name" = %s, "Description" = %s, "Date" = %s, "Hour" = %s, "location" = %s WHERE "EventID" = %s',
            (
                data["name"],
                data["description"],
                data["date"],
                data["time"],
                data["location"],
                EventId,
            ),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


def delete_event(EventId):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM public.event WHERE "EventID" = %s',
            (EventId,),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


# Users

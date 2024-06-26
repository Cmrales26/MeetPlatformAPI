from db import connection_postgreSQL

connection = connection_postgreSQL.connection


def Check_user_in_event(UserID, EventID):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM public.user_event WHERE "_EventID" = %s AND "_UserID" = %s',
            (EventID, UserID),
        )
        user = cursor.fetchone()
        if user is not None:
            return True
        else:
            return False
    except Exception as ex:
        print(ex)
        return False


def Get_Events():
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT public.event.*,public.business."Name" FROM public.event JOIN public.business ON public.event."_BusinessID" = public.business."BusinessID" WHERE public.event."status" = true'
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
                "business_name": event[8],
            }
            event_list.append(event_dict)
        cursor.close()
        return event_list
    except Exception as ex:
        return False


def Get_Event(EventId):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT public.event.*,public.business."Name" FROM public.event JOIN public.business ON public.event."_BusinessID" = public.business."BusinessID" WHERE public.event."EventID" = %s',
            (EventId,),
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
                "business_name": event[8],
            }
            event_list.append(event_dict)
        cursor.close()
        return event_list
    except Exception as ex:
        return False


def get_my_event(UserID):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT public.user_event.*, public.event.*, public.business."Name" FROM public.user_event JOIN public.event ON public.user_event."_EventID" = public.event."EventID" JOIN public.business ON public.event."_BusinessID" = public.business."BusinessID" WHERE public.user_event."_UserID" = %s AND public.event."status" = TRUE;',
            (UserID,),
        )
        events = cursor.fetchall()
        event_list = []
        if len(events) == 0:
            return event_list

        for event in events:
            event_dict = {
                "id": event[3],
                "name": event[4],
                "description": event[5],
                "businessID": event[6],
                "date": event[7].isoformat(),
                "time": event[8].isoformat(),
                "location": event[9],
                "business_name": event[11],
            }
            event_list.append(event_dict)
        return event_list
    except Exception as ex:
        print(ex)


def JoinEvent(UserID, eventID):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO public.user_event ("_UserID", "_EventID") VALUES (%s, %s)',
            (UserID, eventID),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        print(ex)
        return False


def LeaveEvent(userID, eventID):
    try:
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM public.user_event WHERE "_UserID" = %s AND "_EventID" = %s',
            (userID, eventID),
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        print(ex)
        return False

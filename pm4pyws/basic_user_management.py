import sqlite3


class BasicUserManagement(object):
    def check_session_validity(self, session_id):
        """
        Checks the validity of a session

        Parameters
        ------------
        session_id
            Session ID

        Returns
        ------------
        boolean
            Boolean value
        """
        validity = False
        conn_users = sqlite3.connect('users.db')
        curs_users = conn_users.cursor()
        sid = str(session_id)
        curs_users.execute("SELECT USER_ID FROM SESSIONS WHERE SESSION_ID = ? AND SESSION_ID = ?", (sid, sid))
        for res in curs_users.fetchone():
            validity = True
        conn_users.close()
        return validity

    def get_user_from_session(self, session_id):
        """
        Gets the user from the session

        Parameters
        ------------
        session_id
            Session ID

        Returns
        ------------
        user
            User ID
        """
        user = None
        conn_users = sqlite3.connect('users.db')
        curs_users = conn_users.cursor()
        sid = str(session_id)
        curs_users.execute("SELECT USER_ID FROM SESSIONS WHERE SESSION_ID = ? AND SESSION_ID = ?", (sid, sid))
        for res in curs_users.fetchone():
            user = str(res)
        conn_users.close()
        return user

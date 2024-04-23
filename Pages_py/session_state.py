import streamlit as st
from table_model import cursor, connection

class SessionState:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        if username:
            sql = "SELECT id FROM user WHERE username = %s"
            data = (username,)
            cursor.execute(sql, data)
            result = cursor.fetchone()
            if result:
                self.userid = result[0]
            else:
                self.userid = None
        else:
            self.userid = None

    def return_userid(self):
        return self.userid

    def logout(self):
        self.userid = None

    # @staticmethod
    # def get(username=None, password=None):
    #     """Gets a SessionState object for the current session. Creates one if it doesn't exist."""
    #     if 'session' not in st.session_state:
    #         st.session_state.session = SessionState(username, password)
    #     else:
    #         st.session_state.session.username = username
    #         st.session_state.session.password = password
    #     return st.session_state.session

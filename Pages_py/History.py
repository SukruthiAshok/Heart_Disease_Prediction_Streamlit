import streamlit as st
from table_model import cursor, connection
import pandas as pd

user_id=None
def process_data(userid):
    global user_id
    user_id = userid


def history():
    st.title('History Data Viewer')
    st.write("Displaying history from the MySQL database")

    
    # Query to fetch all records from the 'history' table
    query = "SELECT * FROM user_data WHERE userid = %s"
    data=(user_id, )

    # Execute the query and fetch results into a DataFrame
    cursor.execute(query,data)
    columns = [desc[0] for desc in cursor.description]  # Get column names
    data = cursor.fetchall()

    # Create a DataFrame from the data and column names
    df = pd.DataFrame(data, columns=columns)

    # Display the DataFrame in Streamlit
    st.dataframe(df)

    # Close the cursor and the connection
    # cursor.close()
    

# Run the Streamlit app
# if _name_ == '_main_':
#     history()
# Text-to-SQL LLM Application for Querying SQL Databases Using Google Gemini Pro

Many end-users and stakeholders prefer to gain insights from a database using natural language, especially when direct access cannot be granted. 

But how can this be achieved?

This can be accomplished with the help of Google Gemini Pro LLM.

Guided by Krish Sir, I had worked on building a Text-to-SQL LLM application that queries SQL databases using Gemini Pro.

<b>Objective:</b>

The main goal of this project is to convert natural language text into SQL queries using the Gemini Pro LLM application. 
This allows users to input their queries in natural language, which are then converted to SQL queries and executed on the database.

The project has been implemented with SQLite but is adaptable to other databases such as MySQL, MSSQL, etc. <br>


<b>Implementation Steps:</b>
<ol>
  <li><b>Database Setup:</b></li>
    <ul> 
      <li>Use SQLite to create and populate the database with sample records using Python.</li>
    </ul><br>

   <li><b>LLM Integration:</b></li>

<ul> 
      <li>Utilize Google Gemini Pro LLM to build an application that converts natural language queries into SQL queries.</li>
      <li>The generated SQL queries are then executed on the SQL database.</li>
</ul> 
</ol><br>
<b>Files Details:</b>
<ol>
  <li><b>requirements.txt</b> - Lists all the libraries that need to be installed.</li>
  <li><b>.env</b> - Contains the Google Gemini API key.</li>
  <li><b>sql.py</b> - Script for creating the database, creating tables, and inserting values.</li>
  <li><b>sqlapp.py</b> - Script for creating the Streamlit app. This is where the entire LLM application is developed.</li>
</ol><br>
Technologies Used:
Language: Python
LLM: Google Gemini Pro
Database: SQLite
Framework: Streamlit
IDE: VS Code


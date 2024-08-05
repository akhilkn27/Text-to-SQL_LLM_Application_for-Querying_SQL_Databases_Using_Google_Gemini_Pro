# Text-to-SQL LLM Application for Querying SQL Databases Using Google Gemini Pro

Many end-users and stakeholders prefer to gain insights from a database using natural language, especially when direct access cannot be granted. 

But how can this be achieved?

This can be accomplished with the help of Google Gemini Pro LLM.

Guided by <a href='https://www.linkedin.com/in/naikkrish/'>Krish Naik</a> Sir, I had worked on building a Text-to-SQL LLM application that queries SQL databases using Gemini Pro.

<h3><b>Objective:</b></h3>

The main goal of this project is to convert natural language text into SQL queries using the Gemini Pro LLM application. 
This allows users to input their queries in natural language, which are then converted to SQL queries and executed on the database.

The project has been implemented with SQLite but is adaptable to other databases such as MySQL, MSSQL, etc. <br>


<h2><b>Implementation Steps:</b></h2>
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
</ol>
<h2><b>Files Details:</b></h2>
<ol>
  <li><b>requirements.txt</b> - Lists all the libraries that need to be installed.</li>
  <li><b>.env</b> - Contains the Google Gemini API key.</li>
  <li><b>sql.py</b> - Script for creating the database, creating tables, and inserting values.</li>
  <li><b>sqlapp.py</b> - Script for creating the Streamlit app. This is where the entire LLM application is developed.</li>
</ol>

<h2><b>Technologies Used:</b></h2>
<ol>
  <li><b>Language</b> - Python</li>
  <li><b>LLM</b> - Google Gemini Pro</li>
  <li><b>Database</b> - SQLite</li>
  <li><b>Framework</b> - Streamlit</li>
  <li><b>IDE</b> - VS Code</li>
</ol>

<h2>Versions of Module / Libraries</h2>
<ol>
  <li><b>Python</b> :  3.12.0
  <li><b>Streamlit</b> :                     1.37.0</li>
  <li><b>Google-ai-generativelanguage</b> :  0.6.6</li>
  <li><b>Google-api-core</b> :               2.19.1</li>
  <li><b>Google-api-python-client</b> :      2.139.0</li>
  <li><b>Google-auth</b> :                   2.32.0</li>
  <li><b>Google-auth-httplib2</b> :          0.2.0</li>
  <li><b>Google-generativeai</b> :           0.7.2</li>
  <li><b>SQLAlchemy</b> :                    2.0.31</li>
  <li><b>Langchain-google-genai</b> :        1.0.8</li>
  <li><b>Langchain</b> :                     0.2.12</li>
  <li><b>Langchain-community</b> :           0.2.10</li>
  <li><b>Langchain-core</b> :                0.2.27</li>
</ol>

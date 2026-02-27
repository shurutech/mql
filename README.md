# MQL

MQL (My Query Language) is a powerful tool to transform natural language queries into executable SQL queries. What's cool is that anyone can use it, even without knowing how to code. Just add your database by connecting or uploading schema to MQL, ask a query in your language and get the SQL.



https://github.com/shurutech/mql/assets/127201055/43d7dd86-c892-4b4e-a585-46512deb46b9




## 🚀 Getting Started



https://github.com/shurutech/mql/assets/127201055/dac40920-6b22-4758-8f4d-efea9ca121fc



### Run the tool locally using Docker.

- Make sure you have docker installed. 

- To begin, clone this Git repository:

  ```bash
  git clone https://github.com/shurutech/mql
  ```

- Update server/Dockerfile with your `OPENAI_API_KEY` key:
  ```
  ENV OPENAI_API_KEY YOUR_TOKEN_HERE
  ```

- Update the DATABASE_URL in the server/.env file according to the following rules:
  - If you are using docker to run mql, you can use 'postgres' as host name.
  - If you are not using docker to run mql, you can use 'localhost' as host name.

- Navigate to the repository folder and run the following command:
  ```
  make install
  ```

  Once the installation is complete, you can access the MQL dashboard at: http://localhost:3000


---

If needed, you can also restart to reflect local changes, if any, using:
```
make restart
```

Also, you can terminate the local setup using:
```
make down
```

Also, you can start up all the containers using:
```
make up
```

## Use Default Email/Password for Login to Test MQL
A default user is created for login purpose while running the tool using docker. 
  - Email - admin@example.com
  - Password - admin

## Want to Productionize MQL?
Take care of below steps if you are looking to make it Live
  - **Delete default user**: To delete default user(admin@example.com), you need to connect with mql database(mql-postgres) and then remove it from users table. 
  - **Create a new user**:
    - go to project's root directory 
    - exec in backend docker container: docker-compose exec backend /bin/bash 
    - run create_user script: python3 scripts/create_user.py
    - enter email, password and name to create your own user

## Supported Databases

As of the current version, MQL is designed to work exclusively with PostgreSQL. 

----

## **You can also run the tool locally without Docker.**

  - ## Prerequisites

    These are the required packages which needs to be installed to run the project locally.

1. Python

2. psycopg2

3. Node

4. PostgreSQL 15

5. pgvector extension for PostgreSQL - [pgvector](https://github.com/pgvector/pgvector#installation)

- ## Database Setup

  Run these commands in your PostgreSQL command line client

1. **Creating the PostgreSQL Role**

   Create a PostgreSQL role with superuser permissions and login capability:

   ```sql
   CREATE ROLE <role_name> WITH superuser;
   ALTER ROLE <role_name> WITH LOGIN PASSWORD 'password';
   ```

2. **Creating the Databases**

   Create two databases, `mql` and `mql_test`, with the `shuru` role:

   ```sql
   CREATE DATABASE mql WITH OWNER <role_name>;
   CREATE DATABASE mql_test WITH OWNER <role_name>;
   ```

3. **Creating the Extension**

   To create the `vector` extension:

- Connect with the database using:

  ```sql
  \c <databse_name>
  ```

- Create the vector extension:
  ```sql
  CREATE EXTENSION vector;
  ```

- ## Update your env
  
  Update these values at server/.env

  ```env
  DATABASE_URL="postgresql://<role_name>:<password>@<host>:5432/mql"

  TEST_DATABASE_URL="postgresql://<role_name>:<password>@<host>:5432/mql_test"

  OPENAI_API_KEY="<key>"
  ```

  If database is locally hosted then host will be `localhost`

- ## Run the Script

  Navigate to the repository folder and run the command in terminal

  ```bash
  chmod +x ./setup.sh && ./setup.sh
  ```
Once the installation is complete, you can access the MQL dashboard at: http://localhost:3000


## Accuracy Test Score 
Our testing process involved running 50 natural language queries through the MQL platform, with resources like a elearning_schema file, and a CSV of query mappings located in our test_data folder. The MQL achieved around **85% success rate**, accurately translating 43 out of 50 queries. However, when considering the precision of the translations, about 74% (37 out of 50) of the queries were executed perfectly, with 6 queries correctly interpreted but missing a semi-colon at the end. This left us with 7 queries that resulted in errors. We're actively working on enhancements to improve both the accuracy and the completeness of the SQL syntax generation, and we welcome contributions to help refine our platform.
 - We have taken database set from [here](https://github.com/lingyingyang/elearning/blob/master/resources/eldb_bk.sql) for testing purpose.
 - You can remove test_data folder after checking it.

## Next Steps/Features
We plan to continue building after the initial release and look forward to the feedback from the community. As of now we have following features planned out for next releases.

 - Implementation of query execution
 - Improve directly connected dbs and SQL query results
 - Support for MySQL database
 - Improvements in Query Accuracy
 - Show natural language response and data visualisation.
 - User can integrate slack or similar apps to get NL query result there.
 - Test [retool](https://retool.com/products/ai) to generate the queries.


## Contribution Guidelines
We value the contributions of each developer and encourage you to share your ideas, improvements, and fixes with us. To ensure a smooth collaboration process, please follow these guidelines.

Before you begin:

 - Make sure you have a GitHub account.
 - Familiarize yourself with the project by reading the README, exploring the issues, and understanding the tool's architecture and coding standards.

## How to Contribute
**Reporting Bugs**

Before reporting a bug, please:

 - Check the issue tracker to ensure the bug hasn't already been reported.
 - If the issue is unreported, create a new issue, providing:
    - A clear title and description.
    - Steps to reproduce the bug.
    - Expected behavior and what actually happened.
    - Any relevant error messages or screenshots.

**Suggesting Enhancements**
We love to receive suggestions for enhancements! Please:

- First, check if the enhancement has already been suggested.
- If not, open a new issue, describing the enhancement and why it would be beneficial.

**Pull Requests**
Ready to contribute code? Follow these steps:

1. Fork the repository - Create your own fork of the project.
2. Create a new branch for your changes - Keep your branch focused on a single feature or bug fix.
3. Commit your changes - Write clear, concise commit messages that explain your changes.
4. Follow the coding standards - Ensure your code adheres to the coding standards used throughout the project.
5. Write tests - If possible, write tests to cover the new functionality or bug fix.
6. Submit a pull request - Provide a clear description of the problem and solution. Include the relevant issue number if applicable.

**Conduct**
We are committed to providing a welcoming and inspiring community for all. By participating in this project, you are expected to uphold our Code of Conduct, which promotes respect and collaboration.


SOME CHANGES!!!

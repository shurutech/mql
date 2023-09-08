# MQL

MQL is a tool which can be used to ask queries in Natural Langugage and get a SQL query in response which user can run on database to get the result.


## 🚀 Getting Started

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

- Navigate to the repository folder and run the following command:
  ```
  make install
  ```

  Once the installation is complete, you can access the MQL dashboard at: http://localhost:3000


---

If needed, you can also restart the local setup using:
```
make restart
```

Also, you can terminate the local setup using:
```
make down
```

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

   Create two databases, `analytics` and `analytics_test`, with the `shuru` role:

   ```sql
   CREATE DATABASE analytics WITH OWNER <role_name>;
   CREATE DATABASE analytics_test WITH OWNER <role_name>;
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
  DATABASE_URL="postgresql://<role_name>:<password>@<host>:5432/analytics"

  TEST_DATABASE_URL="postgresql://<role_name>:<password>@<host>:5432/analytics_test"

  OPENAI_API_KEY="<key>"
  ```

  If database is locally hosted then host will be `localhost`

- ## Run the Script

  Navigate to the repository folder and run the command in terminal

  ```bash
  chmod +x ./setup.sh && ./setup.sh
  ```
Once the installation is complete, you can access the MQL dashboard at: http://localhost:3000
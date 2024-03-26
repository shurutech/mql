const appText = {
    metadata: {
        title: "Analytics",
        description: "Tool to convert your natural language queries to SQL queries",
    },

    toast: {
        errSessionExpired: "Session expired. Please login again",
        errGeneric: "Something went wrong",
        connectedSuccess: "Connected successfully",
        uploadSuccess: "Uploaded successfully",
        loginSuccess: "Login successful",
    },
    home: {
        login: "Log in",
        features: "Features",
        steps: "Steps",
        title: "Unleash the true potential of your data today!",
        description: "Experience effortless data exploration on our Platform, where you can ask questions in plain English and instantly receive AI-driven insights along with the corresponding SQL queries.",
        insightsEmpowered: "Insights Empowered",
        simplifiedQueries: "Simplified Queries",
        powerfulDecisions: "Powerful Decisions",
        dataEmpowerment: "Data Empowerment",
        insightsEmpoweredDescription: "Discover the power of AI-driven insights, as we revolutionise the way you interact with your data.",
        simplifiedQueriesDescription: "Simplify intricate queries through our user-friendly natural language interface, enabling non-technical users to make informed choices.",
        powerfulDecisionsDescription: "Unleash the true potential of your business with effortless data-driven decision-making.",
        dataEmpowermentDescription: "Unlock the power of AI to harness insights easily, from individual shoppers to global corporations.",
        integrations: "Integrations",
        integrationsDescription: "Discover a Range of Supported Platforms and Explore our growing ecosystem for seamless possibilities",
        stepsTitle: "3 Simple Steps",
        stepsDescription: "Streamline data insights effortlessly with MQL. Just follow 3 simple steps for powerful results.",
        setTheStage: "Set the Stage",
        askAway: "Ask Away",
        queryDelivered: "Voila, Query Delivered",
        setTheStageDescription: "Begin by Connecting Your Database or Uploading Your Database Schema!",
        askAwayDescription: "Pop Your Questions, something like 'How many bookings done in last week?'",
        queryDeliveredDescription: "AI generated working SQL query in your hands!",
    },

    header: {
        features: "Features",
        steps: "Steps",
        dashboard: "Dashboard",
        login: "Log in",
        openMainMenu: "Open main menu",
        closeMenu: "Close menu",
    },

    headerNavbar: {
        home: "Home",
        addDatabase: "Add Database",
        logout: "Logout",
    },

    login: {
        login: "Login",
        email: "Email",
        password: "Password",
        enterEmail: "Enter your email",
        enterPassword: "Enter your password",
    },

    homeDatabases: {
        databases: "Databases",
        added: "Added:",
        viewDb: "View DB",
        askQuery: "Ask Query",
        noDatabase: "No database found. Add database to ask the query.",
    },

    addDatabase: {
        title: "Unleash the true potential of your data today!",
        description: "Easily connect/upload your database schema and experience the power of our AI. Empower your database interactions with power of AI."
    },

    connectDatabase: {
        title: "Connect your Database",
        description: "Please enter your database connection details:",
        connectionString: "Connection String: postgresql://user:password@host:port/database_name",
        databaseName: "Database Name",
        namePlaceholder: "Enter database name",
        databaseUser: "Database User",
        userPlaceholder: "Enter database user",
        databasePassword: "Database Password",
        passwordPlaceholder: "Enter database password",
        databaseHost: "Database Host",
        hostPlaceholder: "Enter database host",
        databasePort: "Database Port",
        portPlaceholder: "Enter database port",
        connect: "Connect",
        or: "OR",
        upload: "Upload",
        yourDatabaseSchema: "your database schema",
    },

    uploadDatabaseSchema: {
        steps: "Steps: Upload database schema",
        firstStep: "1. Copy the curl below and run it on your system. It will fetch a bash script which will generate a schema file for you.",
        secondStep: "2. Now copy the command below to run the bash script and provide the asked parameters. Run the command in the same directory in which you ran the curl command.",
        thirdStep: "3. Now upload the generated schema file to the form below.",
        chooseFileTitle: "Choose the schema file:",
        databaseName: "Database Name",
        upload: "Upload",
        or: "OR",
        connect: "Connect",
        yourDatabase: "your database."
    },


    database: {
        back: "Back",
        home: "Home",
        databaseDetail: "Database Detail",
        description: "Description",
        tableInfo: "Table Info",
        tablesCount: "This database has {tablesCount} tables.",
    },

    chatInterface: {
        back: "Back",
        home: "Home",
        query: "Query",
        history: "History",
        askYourQuery: "Ask your query",
        response: "Response:",
        copy: "Copy",
        queryColon: "Query:",
        queryHistory: "Query History",
        queryHistoryDescription: "Your query history is listed below.",
        noQueryHistory: "No query history found.",
    },

    accordion: {
        columns: "columns",
        columnName: "Column Name",
        dataType: "Data Type",
    },
}

export default appText;

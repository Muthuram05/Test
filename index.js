// Import packages
const express = require("express");
const home = require("./routes/home");
const graphqlData = require('./routes/graphql')
// Middlewares
const app = express();
// app.use(express.json());

// Routes
app.use("/home", graphqlData);

// connection
const port = process.env.PORT || 9001;
app.listen(port, () => console.log(`Listening to port ${port}`));

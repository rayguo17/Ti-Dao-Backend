const express = require("express");
const cors = require("cors")
const { development } = require("./knexfile")
const knex = require('knex')(development)
const morgan = require("morgan")
const redis = require("redis")

const app = express();
const server = require("http").createServer(app);
app.use(express.json());
app.use(morgan("dev"))
app.use(cors())

const redisClient = redis.createClient({
    host: "localhost",
    port: 16379
})


app.get("/ping", (req, res) => {
    res.send("Pong")
})




server.listen(8001, () => {
    console.log("Server running on port 8001...")
})

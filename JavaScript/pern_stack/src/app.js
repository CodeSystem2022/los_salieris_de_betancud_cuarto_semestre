import express from "express";
import morgan from "morgan";

import tareasRouter from "./router/tareas.routes.js";
import authRouter from "./router/auth.routes.js";

const app = express();

app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.use("/api", tareasRouter)
app.use("/api", authRouter)

app.get("/", (req, res) => res.json({message: "Bienvenidos a mi proyecto"}));

app.use((err, req, res, next) => {
    res.status(500).json({
        status: "error",
        message: err.message
    })
})

export default app;

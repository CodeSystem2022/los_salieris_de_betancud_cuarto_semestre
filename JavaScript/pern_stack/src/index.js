import app from "./app.js";
// import {pool} from "./db.js"


/* pool.query("SELECT NOW()",(err,res)=>{
    console.log(err,res.rows);
    pool.end();
}) */

const PORT = process.env.PORT || 3000
    
app.listen(PORT);
console.log("Server on port", PORT);
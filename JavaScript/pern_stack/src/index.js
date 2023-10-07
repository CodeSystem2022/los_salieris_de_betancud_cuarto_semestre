import app from "./app.js";

import { pool } from "./db.js";

const PORT = process.env.PORT || 3000

// pool.query("SELECT now()", (err, res) => {
//     console.log(err, res.rows);
//     pool.end()
// })
app.listen(PORT);
console.log('Server on port', PORT);
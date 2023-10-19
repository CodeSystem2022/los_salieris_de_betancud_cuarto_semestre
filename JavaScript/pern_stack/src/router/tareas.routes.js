import Router from "express-promise-router";
import { listarTareas } from "../controllers/tareas.controller.js";
import { listarTarea } from "../controllers/tareas.controller.js";
import { crearTarea } from "../controllers/tareas.controller.js";
import { actualizarTarea } from "../controllers/tareas.controller.js";
import { eliminarTarea } from "../controllers/tareas.controller.js";
import { isAtuh } from "../middlewares/auth.middleware.js";


const router = Router();

router.get('/tareas', isAtuh, listarTareas);

router.get('/tarea/:id',listarTarea);

router.post('/tareas', crearTarea);

router.put('/tarea/:id', actualizarTarea);

router.delete('/tarea/:id', eliminarTarea);

export default router;
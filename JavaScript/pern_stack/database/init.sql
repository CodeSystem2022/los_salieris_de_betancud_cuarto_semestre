CREATE TABLE IF NOT EXISTS tareas (
  	id SERIAL PRIMARY KEY,
  	titulo varchar(50) UNIQUE NOT NULL,
  	descripcion TEXT
);
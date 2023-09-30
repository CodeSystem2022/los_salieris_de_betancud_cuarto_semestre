package utn.estudiantes;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.modelo.Estudiantes2022;
import utn.estudiantes.servicios.EstudianteServicio;

import java.util.List;
import java.util.Scanner;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
	@Autowired
	private EstudianteServicio estudianteServicio;
	private static final Logger logger = LoggerFactory.getLogger(EstudiantesApplication.class);

	String nl = System.lineSeparator();
	public static void main(String[] args) {
		logger.info("Iniciamos la aplicación...");
		// Levantar la fábrica de spring
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("Aplicación Finalizada.!");
	}

	@Override
	public void run(String... args) throws Exception {
		logger.info(nl + "Ejecutando el método 'run' de Spring..." + nl);
		boolean salir = false;
		Scanner consola = new Scanner(System.in);
		while (!salir) {
			mostrarMenu();
			salir = ejecutarOpciones(consola);
			logger.info(nl);;
		}
	}

	private void mostrarMenu() {
		logger.info("""
      		******* Sistema de Estudiantes *******
      		1. Listar Estudiantes
      		2. Buscar Estudiante
      		3. Agregar Estudiante
      		4. Modificar Estudiante
      		5. Eliminar Estudiante
      		6. Salir
      		
      		Elija una opción:"""
		);
	}

	private boolean ejecutarOpciones(Scanner scanner) {
		int opcion = Integer.parseInt(scanner.nextLine());
		boolean salir = false;
		switch (opcion) {
			case 1 -> {
				logger.info(nl + "Listado de estudiantes" + nl);
				List<Estudiantes2022> estudiantes = estudianteServicio.listarEstudiantes();
				estudiantes.forEach(estudiante -> logger.info(estudiante.toString() + nl));
			} // Fin switch
			case 2 -> {
				logger.info("Digite el id del estudiante a buscar");
				int idEstudiante = Integer.parseInt(scanner.nextLine());
				Estudiantes2022 estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if (estudiante != null) {
					logger.info("Estudiante encontrado: " + estudiante.toString() + nl);
				} else {
					logger.info("Estudiante no encontrado" + nl);
				}
			}
			case 3 -> {
				logger.info("Agregar estudiante:" + nl);
				logger.info("Nombre: ");
				String nombre = scanner.nextLine();
				logger.info("Apellido: ");
				String apellido = scanner.nextLine();
				logger.info("Email: ");
				String email = scanner.nextLine();
				logger.info("Teléfono: ");
				String telefono = scanner.nextLine();
				Estudiantes2022 estudiante = new Estudiantes2022();
				estudiante.setNombre(nombre);
				estudiante.setApellido(apellido);
				estudiante.setEmail(email);
				estudiante.setTelefono(telefono);
				estudianteServicio.guardarEstudiante(estudiante);
				logger.info("Estudiante agregado: " + estudiante.toString() + nl);
			}
			case 4 -> {
				logger.info("Modificar estudiante" + nl);
				logger.info("Ingrese el idEstudiante: ");
				int idEstudiante = Integer.parseInt(scanner.nextLine());
				Estudiantes2022 estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if (estudiante == null) {
					logger.info("Nombre: ");
					String nombre = scanner.nextLine();
					logger.info("Apellido: ");
					String apellido = scanner.nextLine();
					logger.info("Email: ");
					String email = scanner.nextLine();
					logger.info("Teléfono: ");
					String telefono = scanner.nextLine();
					estudiante.setNombre(nombre);
					estudiante.setApellido(apellido);
					estudiante.setEmail(email);
					estudiante.setTelefono(telefono);
					estudianteServicio.guardarEstudiante(estudiante);
					logger.info("Estudiante modificado: " + estudiante.toString() + nl);
				} else {
					logger.info("Estudiante no encontrado");
				}
			}
			case 5 -> {
				logger.info("Eliminar estudiante" + nl);
				logger.info("Digite el id del estudiante: ");
				int idEstudiante = Integer.parseInt(scanner.nextLine());
				Estudiantes2022 estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if (estudiante != null) {
					estudianteServicio.eliminarEstudiante(estudiante);
					logger.info("Estudiante eliminado " + estudiante.toString() + nl);
				} else {
					logger.info("Estudiante no encontrado");
				}
			}
			case 6 -> {
				logger.info("Hasta pronto!" + nl + nl);
				salir	= true;
			}
			default -> logger.info("Opción no reconocida: " + opcion + nl);
		} // Fin switch
		return  salir;
	} // Fin ejecutarOpcion
}
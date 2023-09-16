package utn.estudiantes.servicios;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.estudiantes.modelo.Estudiante;
import utn.estudiantes.repositorio.EstudianteRepositorio;

import java.util.List;

@Service
public class EstudianteServicio implements IEstudianteServicio {
   @Autowired
   private EstudianteRepositorio estudianteRepositorio;

   @Override
   public List<Estudiante> listarEstudiantes() {
      return this.estudianteRepositorio.findAll();
   }

   @Override
   public Estudiante buscarEstudiantePorId(Integer idEstudiante) {
      return this.estudianteRepositorio.findById(idEstudiante).orElse(null);
   }

   @Override
   public void guardarEstudiante(Estudiante estudiante) {
      this.estudianteRepositorio.save(estudiante);
   }

   @Override
   public void eliminarEstudiante(Estudiante estudiante) {
      this.estudianteRepositorio.delete(estudiante);
   }
}

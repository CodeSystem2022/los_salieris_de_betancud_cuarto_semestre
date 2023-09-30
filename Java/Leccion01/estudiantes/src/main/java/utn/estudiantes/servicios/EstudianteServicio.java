package utn.estudiantes.servicios;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.estudiantes.modelo.Estudiantes2022;
import utn.estudiantes.repositorio.EstudianteRepositorio;

import java.util.List;

@Service
public class EstudianteServicio implements IEstudianteServicio {
   @Autowired
   private EstudianteRepositorio estudianteRepositorio;

   @Override
   public List<Estudiantes2022> listarEstudiantes() {
      return this.estudianteRepositorio.findAll();
   }

   @Override
   public Estudiantes2022 buscarEstudiantePorId(Integer idEstudiante) {
      return this.estudianteRepositorio.findById(idEstudiante).orElse(null);
   }

   @Override
   public void guardarEstudiante(Estudiantes2022 estudiante) {
      this.estudianteRepositorio.save(estudiante);
   }

   @Override
   public void eliminarEstudiante(Estudiantes2022 estudiante) {
      this.estudianteRepositorio.delete(estudiante);
   }
}

package utn.tienda_libros.servicio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.tienda_libros.modelo.Libro;
import utn.tienda_libros.repositorio.LibroRepositorio;

import java.util.List;
import java.util.Optional;

@Service
public class LibroServicio implements ILibroServicio {

   @Autowired
   private LibroRepositorio libroRepositorio;

   @Override
   public List<Libro> listarLibros() {
      return libroRepositorio.findAll();
   }

   @Override
   public Optional<Libro> buscarLibroPorId(Integer id) {
      return libroRepositorio.findById(id);
   }

   @Override
   public void guardarLibro(Libro libro) {
      libroRepositorio.save(libro);
   }

   @Override
   public void eliminarLibro(Libro libro) {
      libroRepositorio.delete(libro);
   }
}

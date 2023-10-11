package utn.tienda_libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import utn.tienda_libros.servicio.LibroServicio;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

@Component
public class LibroFrom extends JFrame {
   LibroServicio libroServicio;
   private JPanel panel;
   private JTable tablaLibros;
   private DefaultTableModel tablaModeloLibros;

   @Autowired
   public LibroFrom(LibroServicio libroServicio) {
      this.libroServicio = libroServicio;
      iniciarForma();
   }

   private void iniciarForma(){
      setContentPane(panel);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setVisible(true);
      setSize(900, 700);
      // Dimenciones de la ventana
      Toolkit toolkit = Toolkit.getDefaultToolkit();
      Dimension tamanioPantalla = toolkit.getScreenSize();
      int x = (tamanioPantalla.width - getWidth() / 2);
      int y = (tamanioPantalla.height - getHeight() / 2);
      setLocation(x, y);

   }

   private void createUIComponents() {
      this.tablaModeloLibros = new DefaultTableModel(0, 5);
      String[] cabecera = {"Id", "Libro", "Autor", "Precio", "Existencias"};
      this.tablaModeloLibros.setColumnIdentifiers(cabecera);
      this.tablaLibros = new JTable(tablaModeloLibros);
      this.listarLibros();
   }

   private void listarLibros() {
      // Limpia la tabla
      this.tablaModeloLibros.setRowCount(0);
      // Obtiene los libros de la base de datos
      var libros = libroServicio.listarLibros();
      // Agrega los libros a la tabla
      libros.forEach((libro) -> {
         Object[] renglonLibro = {
               libro.getId(),
               libro.getNombreLibro(),
               libro.getAutor(),
               libro.getPrecio(),
               libro.getExistencias()
         };
         this.tablaModeloLibros.addRow(renglonLibro);
      });
   }
}

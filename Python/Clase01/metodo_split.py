# help(str.split)

cursos = 'Java JavaScript Node Python Diseno'
lista_cursos = cursos.split()
print('Lista de cursos:', lista_cursos, type(lista_cursos))

cursos_separados_coma = 'Java,Python,Node,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split(',', 2)
print('Lista de cursos:', lista_cursos, len(lista_cursos))
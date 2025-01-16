# 2. Clientes y Colegios

**Funcionalidad:** Este grupo gestiona las interacciones entre estudiantes (clientes) y colegios. Permite agregar colegios, cursos y estudiantes, así como inscribir a estudiantes en cursos y gestionar sus exámenes. Los comandos permiten ver listas de estudiantes, cursos y exámenes, así como manejar el proceso de admisión y matrícula en los colegios.

## Comandos a utilizar

- **school add_school <school_name>**: Agregar un nuevo colegio al sistema.
- **school create_course <course_name>**: Crear un nuevo curso en el colegio.
- **client add_client <client_name>**: Agregar un cliente (estudiante) al sistema.
- **client enroll_in_school <client_name> <school_name>**: Inscribir a un cliente en un colegio específico.
- **client leave_school <client_name>**: Permitir que un cliente abandone el colegio.
- **school show_students <school_name>:** Mostrar la lista de estudiantes inscritos en el colegio.
- **client join_enrollment_queue <client_name> <school_name><course_name>**: Poner a un cliente en cola para inscribirse en un curso.
- **school show_enrollment_queue <school_name><course>**: Mostrar la lista de clientes en cola para inscribirse en un curso.
- **school admit_student_from_queue <school_name><course_name>**: Admitir al siguiente cliente en la cola para inscribirse en un curso.
- **school show_courses <school_name>**: Mostrar la lista de cursos disponibles en el colegio.
- **school remove_student <school_name> <client_name>**: Retirar a un cliente del colegio.
- **client assist_course <school_name> <couser_name>**: asistir a un curso en un colegio
- **school show_list**: muestra la lista de colegios en el sistema
- **client show_list**: muestra la lista de clientes en el sistema
- **school close / open <schol_name>**: abrir / cerrar colegio, si no hay alumnos en clase
- **school add_exam_to_course <school_name> <course_name> <exam_name>**: Agregar un examen a un curso específico en el colegio.
- **client take_exam <client_name> <course_name> <exam_name>**: Permitir que un cliente presente un examen de un curso en el que está inscrito.
- **school grade_exam <school_name> <course_name> <client_name> <exam_name> <grade>**: Calificar un examen que un cliente ha presentado en un curso.
- **school remove_exam_from_course <school_name> <course_name> <exam_name>**: Eliminar un examen de un curso si ningún cliente lo ha presentado.
- **school show_exams <school_name> <course_name>**: Mostrar la lista de exámenes disponibles para un curso en el colegio.
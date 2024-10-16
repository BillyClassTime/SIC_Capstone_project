# 1. Supermercados y Clientes

**Funcionalidad:** Este grupo se encarga de gestionar las operaciones de un supermercado y sus clientes. Permite agregar supermercados, productos, y clientes, así como realizar acciones relacionadas con las compras, como recoger productos, pagar cuentas, y gestionar el inventario del supermercado. Los comandos permiten también el manejo de la caja y la interacción entre clientes y el personal del supermercado.

## Comandos ha utilizar

- **school add <school_name>**: Agregar un nuevo colegio al sistema.
- **school create_course <course_name>**: Crear un nuevo curso en el colegio.
- **client add <client_name>**: Agregar un cliente (estudiante) al sistema.
- **client enroll <client_name> <school_name>**: Inscribir a un cliente en un colegio específico.
- **client leave <client_name>**: Permitir que un cliente abandone el colegio.
- **school show_students <school_name>**: Mostrar la lista de estudiantes inscritos en el colegio.
- **client join_enrollment_queue <client_name> <school_name> <course_name>**: Poner a un cliente en cola para inscribirse en un curso.
- **school show_enrollment_queue <school_name> <course_name>**: Mostrar la lista de clientes en cola para inscribirse en un curso.
- **school admit_from_queue <school_name> <course_name>**: Admitir al siguiente cliente en la cola para inscribirse en un curso.
- **school show_courses <school_name>**: Mostrar la lista de cursos disponibles en el colegio.
- **school remove_student <school_name> <client_name>**: Retirar a un cliente del colegio.
- **client assist_course <course_name>**: Permitir que un cliente asista a un curso.
- **school show_list**: Mostrar la lista de colegios en el sistema.
- **client show_list**: Mostrar la lista de clientes en el sistema.
- **school set_open_close <school_name> <open/close>**: Abrir / Cerrar el colegio, si no hay alumnos en clase.
- **school add_exam <school_name> <course_name> <exam_name>**: Agregar un examen a un curso específico en el colegio.
- **client take_exam <client_name> <course_name> <exam_name>**: Permitir que un cliente presente un examen de un curso en el que está inscrito.
- **school grade_exam <school_name> <course_name> <client_name> <exam_name> <grade>**: Calificar un examen que un cliente ha presentado en un curso.
- **school remove_exam <school_name> <course_name> <exam_name>**: Eliminar un examen de un curso si ningún cliente lo ha presentado.
- **school show_exams <school_name> <course_name>**: Mostrar la lista de exámenes disponibles para un curso en el colegio.




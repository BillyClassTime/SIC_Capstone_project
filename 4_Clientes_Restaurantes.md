# 4. Clientes y Restaurantes

**Funcionalidad:** Este grupo maneja las operaciones de restaurantes y la interacción de los clientes con ellos. Permite agregar restaurantes, platos, y gestionar reservas. Los comandos permiten a los clientes realizar pedidos, pagar cuentas, cancelar reservas y consultar menús, así como verificar el historial de pedidos en el restaurante.

## Comandos a utilizar

- **restaurant add <restaurant_name>**: Agregar un nuevo restaurante al sistema.

- **client add <client_name>**: Agregar un cliente al sistema.

- **restaurant add_dish <restaurant_name> <dish_name>**: Agregar un nuevo plato al menú del restaurante.

- **client make_reservation <client_name> <restaurant_name>**: Reservar una mesa en un restaurante específico.

- **client cancel_reservation <client_name> <restaurant_name>**: Cancelar una reserva en un restaurante.

- **restaurant show_menu <restaurant_name>**: Mostrar el menú del restaurante.

- **client order <client_name> <restaurant_name> <dish_name>**: Pedir un plato del menú.

- **restaurant serve_next_order <restaurant_name>**: Atender el siguiente pedido en la cocina.

- **client pay <client_name> <restaurant_name>**: Pagar la cuenta en el restaurante.

- **client leave <client_name> <restaurant_name>**: Permitir que un cliente salga del restaurante después de pagar.

- **restaurant show_order_history <restaurant_name>**: Mostrar el historial de pedidos en el restaurante.

- **client request_bill <client_name> <restaurant_name>**: Solicitar la cuenta en el restaurante.

- **client leave_without_payment <client_name> <restaurant_name>**: Permitir que un cliente se vaya sin pagar, si no ha 

  consumido nada.

- **restaurant show_customers <restaurant_name>**: Mostrar la lista de clientes en el restaurante.

- **client check_wait_time <client_name> <restaurant_name>**: Consultar el tiempo de espera para una mesa.

- **client request_table <client_name> <restaurant_name>**: Solicitar una mesa en el restaurante después de haber hecho una reserva.

- **restaurant show_reservations <restaurant_name>**: Mostrar la lista de reservas realizadas en el restaurante.

- **client enter <client_name> <restaurant_name>**: Permitir que un cliente entre al restaurante, siempre que tenga una reserva.

- **restaurant cancel_order <restaurant_name> <client_name> <dish_name>**: Cancelar el pedido de un cliente antes de que sea servido.

- **restaurant set_open_close <restaurant_name> <open/close>**: Abrir o cerrar el restaurante, siempre que no haya clientes dentro o reservas pendientes.

- **load_agents <file_path>**:  Load agents from a `JSON` file.

- **save_agents <file_path>**: Save agents to a `JSON` file.
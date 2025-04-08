# 5. Clientes y Teatros

**Funcionalidad:** Este grupo se centra en la gestión de teatros y la interacción de los clientes con ellos. Permite agregar teatros y espectáculos, así como realizar reservas y compras de tickets. Los comandos permiten a los clientes entrar y salir del teatro, solicitar reembolsos, y verificar el estado de sus tickets y el horario de eventos.

## Comandos a utilizar

- **theater add <theater_name>**: Agregar un nuevo teatro al sistema.
- **client add <client_name>**: Agregar un cliente al sistema.
- **theater add_show <theater_name> <show_name>**: Agregar un nuevo espectáculo al teatro.
- **client make_reservation <client_name> <theater_name> <show_name>**: Reservar una entrada para un espectáculo en el teatro.
- **client cancel_reservation <client_name> <theater_name> <show_name>**: Cancelar una reserva para un espectáculo en el teatro.
- **theater show_schedule <theater_name>**: Mostrar los espectáculos en el teatro.
- **client buy_ticket <client_name> <theater_name> <show_name>**: Comprar un ticket para un espectáculo.
- **client enter <client_name> <theater_name>**: Permitir que un cliente entre al teatro, siempre que tenga un ticket o reserva.
- **client leave <client_name> <theater_name>**: Permitir que un cliente salga del teatro.
- **theater show_clients <theater_name>**: Mostrar la lista de clientes que están en el teatro.
- **client request_refund <client_name> <theater_name> <show_name>**: Solicitar un reembolso por un ticket comprado.
- **theater remove_show <theater_name> <show_name>**: Eliminar un espectáculo del teatro, siempre que no haya clientes dentro.
- **client check_wait_time <client_name> <theater_name>**: Consultar el tiempo de espera para entrar al teatro.
- **theater show_all_clients**: Mostrar la lista de todos los clientes en el sistema.
- **client go_to_show <client_name> <theater_name> <show_name>**: Indicar que un cliente asiste a un espectáculo.
- **client leave_show <client_name> <theater_name> <show_name>**: Indicar que un cliente sale de un espectáculo.
- **theater show_current_shows <theater_name>**: Mostrar los espectáculos actuales en el teatro.
- **theater show_info <theater_name> <show_name>**: Mostrar información sobre un espectáculo específico en el teatro.
- **client check_ticket_status <client_name> <theater_name> <show_name>**: Consultar el estado de un ticket para un espectáculo.
- **client show_all_clients**: Mostrar la lista de todos los clientes en el sistema.

- **load_agents <file_path>**:  Load agents from a `JSON` file.
- **save_agents <file_path>**: Save agents to a `JSON` file.
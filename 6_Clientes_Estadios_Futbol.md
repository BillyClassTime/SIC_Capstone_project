# 6. Clientes y Estadios de Fútbol

**Funcionalidad:** Este grupo se dedica a gestionar la operación de estadios de fútbol y la experiencia de los clientes en eventos deportivos. Permite agregar estadios y eventos, comprar y cancelar tickets, y gestionar la entrada y salida de los clientes. También incluye funcionalidades para verificar la asistencia a eventos, consultar tiempos de espera, y reportar problemas durante el evento.

## Comandos a utilizar

- **stadium add <stadium_name>**: Agregar un nuevo estadio al sistema.
- **client add <client_name>**: Agregar un cliente al sistema.
- **stadium add_event <stadium_name> <event_name>**: Agregar un nuevo evento (por ejemplo, partido de fútbol) al estadio.
- **client buy_ticket <client_name> <stadium_name> <event_name>**: Comprar un ticket para un evento en el estadio.
- **client cancel_ticket <client_name> <stadium_name> <event_name>**: Cancelar un ticket para un evento en el estadio.
- **stadium show_events <stadium_name>**: Mostrar la lista de eventos próximos en el estadio.
- **client enter <client_name> <stadium_name>**: Permitir que un cliente entre al estadio, siempre que tenga un ticket.
- **client leave <client_name> <stadium_name>**: Permitir que un cliente salga del estadio.
- **stadium show_attendance <stadium_name> <event_name>**: Mostrar la lista de clientes que asisten a un evento específico en el estadio.
- **client request_refund <client_name> <stadium_name> <event_name>**: Solicitar un reembolso por un ticket comprado.
- **stadium remove_event <stadium_name> <event_name>**: Eliminar un evento del estadio, siempre que no haya clientes dentro.
- **client check_wait_time <client_name> <stadium_name>**: Consultar el tiempo de espera para entrar al estadio.
- **stadium show_current_events <stadium_name>**: Mostrar los eventos actuales que se llevan a cabo en el estadio.
- **stadium show_info <stadium_name>**: Mostrar información sobre el estadio (por ejemplo, ubicación, capacidad).
- **client view_ticket_status <client_name> <stadium_name> <event_name>**: Consultar el estado de un ticket para un evento.
- **client cheer_for_team <client_name> <stadium_name> <team_name>**: Indicar que un cliente anima a un equipo específico durante un partido.
- **stadium show_clients <stadium_name>**: Mostrar la lista de clientes que están actualmente en el estadio.
- **client check_event_schedule <client_name> <stadium_name>**: Consultar el calendario de eventos en el estadio.
- **client report_issue <client_name> <stadium_name> <issue_description>**: Reportar un problema o inquietud mientras se encuentra en el estadio.
- **client show_all_clients**: Mostrar la lista de todos los clientes en el sistema

- **load_agents <file_path>**:  Load agents from a `JSON` file.
- **save_agents <file_path>**: Save agents to a `JSON` file.
# Documentación de Casos de Prueba

## Introducción
Este archivo contiene pruebas unitarias para la clase `CitySimulation` y sus funcionalidades principales. Las pruebas están diseñadas para verificar el correcto funcionamiento de los comandos y las restricciones del sistema, incluyendo la interacción entre clientes, ayuntamientos y servicios.

---

## Casos de Prueba

### 1. **test_commands**
Probar los comandos básicos de la simulación, incluyendo la creación de clientes y ayuntamientos, la solicitud de servicios, y la eliminación de entidades.

- **Flujo de prueba**:
  1. Crear un cliente (`Billy`) y un ayuntamiento (`Pinto`).
  2. El cliente entra al ayuntamiento.
  3. Añadir un servicio (`Empadronar`) al ayuntamiento.
  4. El cliente solicita el servicio.
  5. Verificar la cola de servicios del ayuntamiento.
  6. El cliente sale del ayuntamiento.
  7. Intentar salir de un ayuntamiento en el que no está.
  8. Mostrar y eliminar servicios del ayuntamiento.
  9. Eliminar el cliente y el ayuntamiento.

- **Casos especiales**:
  - Verificar el manejo de la cola de servicios con marcas de tiempo.
  - Esperar 10 segundos para cumplir con el umbral de tiempo antes de eliminar el ayuntamiento.

---

### 2. **test_remove_town_hall_with_restrictions**
Prueba las restricciones al intentar eliminar un ayuntamiento.

- **Flujo de prueba**:
  1. Crear un ayuntamiento (`Pinto`) y añadir un servicio (`Empadronar`).
  2. Crear un cliente (`Billy`) y hacer que entre al ayuntamiento.
  3. El cliente solicita un servicio.
  4. Intentar eliminar el ayuntamiento con procesos encolados (debe fallar).
  5. Procesar los servicios en cola y verificar que ya no hay procesos pendientes.
  6. Intentar eliminar el ayuntamiento con servicios activos (debe fallar).
  7. Eliminar el servicio y verificar que ya no hay servicios activos.
  8. Intentar eliminar el ayuntamiento con clientes dentro (debe fallar).
  9. Hacer que el cliente salga del ayuntamiento.
  10. Eliminar el ayuntamiento exitosamente.

---

### 3. **test_client_exit_town_hall**
Prueba el flujo de entrada y salida de un cliente en un ayuntamiento.

- **Flujo de prueba**:
  1. Crear un cliente (`Billy`) y un ayuntamiento (`Pinto`).
  2. El cliente entra al ayuntamiento.
  3. El cliente sale del ayuntamiento.

---

### 4. **test_error_handling**
Prueba el manejo de errores en comandos inválidos o situaciones no permitidas.

- **Flujo de prueba**:
  1. Crear un cliente (`Billy`).
  2. Intentar que el cliente entre a un ayuntamiento inexistente.
  3. Intentar que el cliente salga de un ayuntamiento inexistente.
  4. Crear un ayuntamiento (`Pinto`) y hacer que el cliente entre.
  5. Intentar que el cliente solicite un servicio inexistente.
  6. Intentar eliminar un cliente inexistente.
  7. Intentar eliminar un servicio inexistente de un ayuntamiento.

- **Casos especiales**:
  - Verificar que los mensajes de error sean claros y específicos.

---

## Métodos Auxiliares

### `run_command_and_assert(command, expected_output)`
- **Descripción**: Ejecuta un comando en la simulación y verifica que la salida contenga el texto esperado.
- **Parámetros**:
  - `command`: Comando a ejecutar.
  - `expected_output`: Salida esperada que debe estar presente en el resultado.
- **Comportamiento**:
  - Si la salida contiene el texto esperado, la prueba pasa.
  - Si no, se muestra un mensaje de error detallado y se permite al usuario decidir si continuar o salir.

---

## Ejecución de las Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando en la terminal:

```powershell
python -m unittest test_city_simulation.py
```

## Notas Adicionales

- **Dependencias**:
  - La clase `CitySimulation` debe estar correctamente implementada y disponible en el archivo `CitySimulation.py`.
  - Las pruebas dependen de la funcionalidad de las clases `Client`, `TownHall`, y `AgentManager`.
- **Casos Especiales**:
  - Algunas pruebas incluyen retrasos (`time.sleep`) para cumplir con los umbrales de tiempo definidos en el sistema.
  - Los mensajes de error y las restricciones del sistema son validados en detalle.
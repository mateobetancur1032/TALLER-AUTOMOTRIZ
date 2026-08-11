class Empleado:
    def __init__(self, id_empleado, nombre, telefono, cargo, salario, horario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.cargo = cargo
        self.salario = salario
        self.horario = horario


# Empleados especializados por servicio
empleados_servicio = {
    "Cambio de aceite": Empleado(
        1, "Calvito Lubricador", "3001111111",
        "Lubricador", 2000000, "8AM - 5PM"
    ),

    "Alineación": Empleado(
        2, "Andrés", "3002222222",
        "Técnico de suspensión", 2200000, "8AM - 5PM"
    ),

    "Revisión general": Empleado(
        3, "Laura", "3003333333",
        "Mecánica general", 2500000, "8AM - 5PM"
    ),

    "Frenos": Empleado(
        4, "Miguel", "3004444444",
        "Especialista en frenos", 2400000, "8AM - 5PM"
    ),

    "Diagnóstico": Empleado(
        5, "Sofía", "3005555555",
        "Diagnóstico automotriz", 2600000, "8AM - 5PM"
    )
}
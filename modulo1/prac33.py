class Conductor:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.horarios = []  # Lista de horarios asignados al conductor

class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None  # Ruta asignada al bus
        self.horarios = []  # Horarios del bus
        self.conductores_asignados = []  # Lista de conductores asignados al bus

class Admin:
    def __init__(self):
        self.buses = []  # Lista de buses
        self.conductores = []  # Lista de conductores

    def agregar_bus(self, placa):
        nuevo_bus = Bus(placa)
        self.buses.append(nuevo_bus)
        print(f"Bus con placa {placa} agregado correctamente.")

    def agregar_ruta_a_bus(self, placa, ruta):
        bus = self.buscar_bus(placa)
        if bus:
            bus.ruta = ruta
            print(f"Ruta '{ruta}' asignada al bus con placa {placa}.")
        else:
            print(f"Bus con placa {placa} no encontrado.")

    def registrar_horario_a_bus(self, placa, horario):
        bus = self.buscar_bus(placa)
        if bus:
            if horario not in bus.horarios:
                bus.horarios.append(horario)
                print(f"Horario '{horario}' registrado para el bus con placa {placa}.")
            else:
                print(f"El horario '{horario}' ya está registrado para este bus.")
        else:
            print(f"Bus con placa {placa} no encontrado.")

    def agregar_conductor(self, nombre, dni):
        nuevo_conductor = Conductor(nombre, dni)
        self.conductores.append(nuevo_conductor)
        print(f"Conductor {nombre} con DNI {dni} agregado correctamente.")

    def agregar_horario_a_conductor(self, dni, horario):
        conductor = self.buscar_conductor(dni)
        if conductor:
            if horario not in conductor.horarios:
                conductor.horarios.append(horario)
                print(f"Horario '{horario}' agregado al conductor con DNI {dni}.")
            else:
                print(f"El horario '{horario}' ya está registrado para este conductor.")
        else:
            print(f"Conductor con DNI {dni} no encontrado.")

    def asignar_bus_a_conductor(self, placa, dni, horario):
        bus = self.buscar_bus(placa)
        conductor = self.buscar_conductor(dni)

        if not bus:
            print(f"Bus con placa {placa} no encontrado.")
            return

        if not conductor:
            print(f"Conductor con DNI {dni} no encontrado.")
            return

        if horario in conductor.horarios:
            print(f"El conductor ya tiene asignado el horario '{horario}'.")
            return

        if horario in bus.horarios:
            conductor.horarios.append(horario)
            bus.conductores_asignados.append(conductor)
            print(f"Bus con placa {placa} asignado al conductor {conductor.nombre} en el horario '{horario}'.")
        else:
            print(f"El horario '{horario}' no está registrado en el bus.")

    def buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        return None

    def buscar_conductor(self, dni):
        for conductor in self.conductores:
            if conductor.dni == dni:
                return conductor
        return None

    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                self.agregar_bus(placa)
            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta del bus: ")
                self.agregar_ruta_a_bus(placa, ruta)
            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                horario = input("Ingrese el horario del bus (HH:MM): ")
                self.registrar_horario_a_bus(placa, horario)
            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                dni = input("Ingrese el DNI del conductor: ")
                self.agregar_conductor(nombre, dni)
            elif opcion == "5":
                dni = input("Ingrese el DNI del conductor: ")
                horario = input("Ingrese el horario del conductor (HH:MM): ")
                self.agregar_horario_a_conductor(dni, horario)
            elif opcion == "6":
                placa = input("Ingrese la placa del bus: ")
                dni = input("Ingrese el DNI del conductor: ")
                horario = input("Ingrese el horario de asignación (HH:MM): ")
                self.asignar_bus_a_conductor(placa, dni, horario)
            elif opcion == "7":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    admin = Admin()
    admin.mostrar_menu()

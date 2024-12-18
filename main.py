class PowerSupply:

    def __init__(self, power):
        self.__power = power

    def apply_voltage(self):
        return f"Подаем напряжение мощностью {self.__power}"

class Motherboard:

    def __init__(self, chipset):
        self.__chipset = chipset

    def redistribute_the_voltage(self):
        return f"Перераспределяем напряжение от БП по компонентам с чипсетом {self.__chipset}"

class CPU:

    def __init__(self, clock_speed, core_number):
        self.__clock_speed = clock_speed
        self.__core_number = core_number

    def activate_turbo_mode(self):
        return f"Активация турбо режима на частоте {self.__clock_speed}"

class RAM:
    def __init__(self, memory_size, memory_frequency):
        self.__memory_size = memory_size
        self.__memory_frequency = memory_frequency

    def load_data(self):
        return f"Загружаем данные в ОЗУ объемом {self.__memory_size}"


    def unload_data(self):
       return f"Выгружаем данные из ОЗУ {self.__memory_size}"

class SSD:
    def __init__(self, capacity):
        self.__capacity = capacity

    def save_data(self):
        return f"Данные сохранены на SDD-накопителе {self.__capacity}"

    def delete_data(self):
        return f"Данные удалены из SDD-накопителя {self.__capacity}"


class GPU:
    def __init__(self, model, memory):
        self.__model = model
        self.__memory = memory

    def display_image(self):
        return f"Изображение выведено на экран {self.__model} "


class PersonalComputer(PowerSupply, Motherboard, CPU, RAM, SSD, GPU):
    def __init__(self, power, chipset, clock_speed, core_number, memory_size, memory_frequency, capacity, model, memory ):
        PowerSupply.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, clock_speed, core_number)
        RAM.__init__(self, memory_size, memory_frequency)
        SSD.__init__(self, capacity)
        GPU.__init__(self, model, memory)


personal_computer = PersonalComputer(500, "X470", 3.8, 8, 16, 3200, 500, "Nvidia GTX 1080", 8)
print(personal_computer.apply_voltage())
print(personal_computer.redistribute_the_voltage())
print(personal_computer.activate_turbo_mode())
print(personal_computer.load_data())
print(personal_computer.unload_data())
print(personal_computer.save_data())
print(personal_computer.delete_data())
print(personal_computer.display_image())


class PersonalComputerComp:

    def __init__(self, powersupply_obj: object = PowerSupply, motherboard_obj: object = Motherboard, cpu_obj: object = CPU, ram_obj: object = RAM, ssd_obj: object = SSD, gpu_obj: object = GPU):
        self.powersupply = powersupply_obj
        self.motherboard = motherboard_obj
        self.cpu = cpu_obj
        self.ram = ram_obj
        self.ssd = ssd_obj
        self.gpu = gpu_obj

powersupply = PowerSupply('500')
motherboard = Motherboard('X470')
cpu = CPU('3.8','8')
ram = RAM('16','3200')
ssd = SSD('500')
gpu = GPU('Nvidia GTX 1080', '8')
computer = PersonalComputerComp(powersupply, motherboard, cpu, ram, ssd, gpu)
print(computer.powersupply)
print(computer.motherboard)
print(computer.cpu)
print(computer.ram)
print(computer.ssd)
print(computer.gpu)
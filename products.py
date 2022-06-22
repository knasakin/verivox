from migration import *


class BasicTariff:  # Продукт обычного тарифа
    def __init__(self, base_costs_per_month: int, consumption_costs: int):
        self.name = 'Basic electricity tariff'
        self.base_costs_per_year = base_costs_per_month * 12  # €/year
        self.consumption_costs = consumption_costs / 100  # €/kWh

    def calculate_annual_costs(self, consumption: int):  # принимает kWh/year
        annual_costs = self.base_costs_per_year + (consumption * self.consumption_costs)
        return int(annual_costs)  # возвращает €/year


class PackagedTariff:  # Продукт пакетного тарифа
    def __init__(self, tariff_price: int, tariff_consumption: int, additional_costs: int):
        self.name = 'Packaged tariff'
        self.tariff_price = tariff_price  # €/year
        self.tariff_consumption = tariff_consumption  # kWh/year
        self.additional_costs = additional_costs / 100  # €/kWh

    def calculate_annual_costs(self, consumption: int):  # принимает kWh/year
        if consumption <= self.tariff_consumption:
            return self.tariff_price  # возвращает €/year

        additional_consumption = consumption - self.tariff_consumption  # kWh/year
        total_costs = self.tariff_price + (self.additional_costs * additional_consumption)
        return int(total_costs)  # возвращает €/year


def get_products():  # формирую список продуктов из БД
    objects = []

    for obj in cursor.execute('SELECT * FROM products'):  # obj вида ('basic',
        if 'basic' in obj:
            objects.append(BasicTariff(obj[1], obj[2]))
        elif 'package' in obj:
            objects.append(PackagedTariff(obj[3], obj[4], obj[5]))

    return objects

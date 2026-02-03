class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

    def mark_as_rented(self):
        print("Метод буде реалізовано пізніше.")

    def mark_as_available(self):
        print("Метод буде реалізовано пізніше.")


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name

    def view_available_cars(self, rental_system):
        print("Метод буде реалізовано пізніше.")

    def book_car(self, car, rental_system):
        print("Метод буде реалізовано пізніше.")


class Rental:
    def __init__(self, rental_id, client, car, rental_days):
        self.rental_id = rental_id
        self.client = client
        self.car = car
        self.rental_days = rental_days

    def create_rental(self):
        print("Метод буде реалізовано пізніше.")

    def close_rental(self):
        print("Метод буде реалізовано пізніше.")


class RentalConfirmation:
    def __init__(self, rental):
        self.rental = rental

    def generate_confirmation(self):
        print("Метод буде реалізовано пізніше.")

    def print_confirmation(self):
        print("Метод буде реалізовано пізніше.")


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.rentals = []

    def add_car(self, car):
        print("Метод буде реалізовано пізніше.")

    def get_available_cars(self):
        print("Метод буде реалізовано пізніше.")

    def create_rental(self, client, car, days):
        print("Метод буде реалізовано пізніше.")


if __name__ == "__main__":
    rental_system = CarRentalSystem()

    car1 = Car(1, "Toyota", "Corolla", 50)
    car2 = Car(2, "BMW", "X5", 120)

    rental_system.add_car(car1)
    rental_system.add_car(car2)

    client = Client(1, "Іван Петренко")

    client.view_available_cars(rental_system)

    rental = rental_system.create_rental(client, car1, 3)

    confirmation = RentalConfirmation(rental)
    confirmation.generate_confirmation()
    confirmation.print_confirmation()
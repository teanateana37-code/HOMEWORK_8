import pandas as pd

class Car:
    def __init__(self, car_id, brand, model, price_per_day, is_available):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = is_available

    def __str__(self):
        return f"{self.car_id}: {self.brand} {self.model} - ${self.price_per_day}/day"

class Client:
    def __init__(self, name):
        self.name = name

    def view_available_cars(self, system):
        system.show_available_cars()

    def book_car(self, system, car_id, days):
        return system.create_rental(self, car_id, days)

class Rental:
    def __init__(self, client, car, days):
        self.client = client
        self.car = car
        self.days = days
        self.total_price = days * car.price_per_day

class RentalConfirmation:
    def __init__(self, rental):
        self.rental = rental

    def print_confirmation(self):
        print("\n===== RENTAL CONFIRMATION =====")
        print(f"Client: {self.rental.client.name}")
        print(f"Car: {self.rental.car.brand} {self.rental.car.model}")
        print(f"Days: {self.rental.days}")
        print(f"Total price: ${self.rental.total_price}")
        print("===============================\n")

class CarRentalSystem:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.load_data()

    def load_data(self):
        self.df = pd.read_csv(self.csv_file)

    def save_data(self):
        self.df.to_csv(self.csv_file, index=False)

    def show_available_cars(self):
        available = self.df[self.df["is_available"] == True]

        if available.empty:
            print("No cars available.")
            return

        print("\nAvailable cars:")
        for _, row in available.iterrows():
            car = Car(
                row["car_id"],
                row["brand"],
                row["model"],
                row["price_per_day"],
                row["is_available"]
            )
            print(car)
        print()

    def get_car_by_id(self, car_id):
        car_row = self.df[self.df["car_id"] == car_id]

        if car_row.empty:
            return None

        row = car_row.iloc[0]
        return Car(
            row["car_id"],
            row["brand"],
            row["model"],
            row["price_per_day"],
            row["is_available"]
        )

    def create_rental(self, client, car_id, days):
        car = self.get_car_by_id(car_id)

        if not car:
            print("Car not found.")
            return None

        if not car.is_available:
            print("Car is already rented.")
            return None

        self.df.loc[self.df["car_id"] == car_id, "is_available"] = False
        self.save_data()

        rental = Rental(client, car, days)
        confirmation = RentalConfirmation(rental)
        confirmation.print_confirmation()

        return rental

if __name__ == "__main__":
    system = CarRentalSystem("cars.csv")

    name = input("Enter your name: ")
    client = Client(name)

    while True:
        print("1. View available cars")
        print("2. Rent a car")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            client.view_available_cars(system)

        elif choice == "2":
            car_id = int(input("Enter car ID: "))
            days = int(input("Enter number of days: "))
            client.book_car(system, car_id, days)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
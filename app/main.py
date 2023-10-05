from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    list_of_customers_obj = [Customer(customer["name"], customer["food"])
                             for customer in customers]

    for customer in list_of_customers_obj:
        cinema_bar.sell_product(customer, customer.food)
    hall.movie_session(movie, list_of_customers_obj, cleaner_obj)

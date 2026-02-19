def get_user_input():
    age = int(input("Enter your age: "))
    seat_type = input("Seat type (Premium / Gold / Regular): ")
    show_type = input("Show type (Movie / Concert / Drama): ")
    show_time = input("Show time (Morning / Afternoon / Evening): ")

    is_member = input("Are you a member? (yes/no): ").lower() == "yes"
    is_weekend = input("Is it weekend? (yes/no): ").lower() == "yes"

    return age, seat_type, show_type, show_time, is_member, is_weekend


def check_age_eligibility(age):
    if age > 17:
        print("You are eligible to book a ticket")
        return True
    else:
        print("You are not eligible to book a ticket")
        return False


def check_evening_show_eligibility(age, show_time):
    if show_time == "Evening":
        if age >= 21:
            print("User is eligible for Evening shows")
            return True
        else:
            print("User is not eligible for Evening shows")
            return False
    return True


def calculate_discount(is_member, age):
    if is_member and age >= 21:
        print("User qualifies for membership discount")
        return 3
    print("User does not qualify for membership discount")
    return 0


def calculate_extra_charges(is_weekend, show_time):
    if is_weekend or show_time == "Evening":
        print("Extra charges will be applied")
        return 2
    print("No extra charges will be applied")
    return 0


def calculate_service_charges(seat_type):
    if seat_type == "Premium":
        return 5
    elif seat_type == "Gold":
        return 3
    else:
        return 1


def booking_allowed(age, show_time, is_member):
    return age >= 21 or (age >= 18 and (show_time != "Evening" or is_member))


def calculate_total_price(base_price, service_charges, extra_charges, discount):
    return base_price + service_charges + extra_charges - discount


def main():
    base_price = 15

    age, seat_type, show_type, show_time, is_member, is_weekend = get_user_input()

    if not check_age_eligibility(age):
        return

    check_evening_show_eligibility(age, show_time)

    discount = calculate_discount(is_member, age)
    extra_charges = calculate_extra_charges(is_weekend, show_time)

    if booking_allowed(age, show_time, is_member):
        print("Ticket booking condition satisfied")

        service_charges = calculate_service_charges(seat_type)
        print("Service charges:", service_charges)

        total_price = calculate_total_price(
            base_price, service_charges, extra_charges, discount
        )
        print("Total Ticket Price:", total_price)

    else:
        print("Ticket booking failed due to restrictions")


main()

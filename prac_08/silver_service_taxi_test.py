from prac_08.silver_service_taxi import SilverServiceTaxi

def main():

    my_silver_taxi = SilverServiceTaxi("taxi1", 100, 2)
    my_silver_taxi.drive(18)
    print(my_silver_taxi.get_fare())
    print(my_silver_taxi)

main()

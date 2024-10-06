airports = {}

while True:
    option = input("Enter 'new' to add an airport, 'fetch' to get an airport name, or 'quit' to exit: ").lower()

    if option == "new":
        icao_code = input("Enter the ICAO code of the airport: ").upper()
        name = input("Enter the name of the airport: ")
        airports[icao_code] = name
    elif option == "fetch":
        icao_code = input("Enter the ICAO code: ").upper()
        if icao_code in airports:
            print(airports[icao_code])
        else:
            print("Airport not found")
    elif option == "quit":
        break
    else:
        print("Invalid option")


Max_Tickets = 100
file_name = "tickets.txt"
def menu():
    print("--------------------[ Concert Even Ticketing System Menu ]--------------------")
    print("[1]. Add Ticket")
    print("[2]. Display All Tickets")
    print("[3]. Search Ticket")
    print("[4]. Update Ticket")
    print("[5]. Delete Ticket")
    print("[6]. Sort by Price")
    print("[7]. Calculate Revenue")
    print("[8]. Save Tickets")
    print("[9]. Exit")
    print("-------------------------------------------------------------------------------")
def id_already_exists(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return True
    return False
def count_VIP(tickets):
    total = 0
    for ticket in tickets:
        if ticket["seat_section"] == "VIP":
            total += 1
    return total
def add_ticket(tickets, vipCapacity):
    print("----------[ Add Ticket ]------------")
    # add id
    while True:
        ticket_id = int(input("Enter your Ticket ID: "))
        if ticket_id <= 0:
            print("Ticket ID cannot be less than zero.")
        elif id_already_exists(tickets, ticket_id):
            print("Ticket ID already exists.")
        else:
            break
    # ask for buyer name
    buyer_name = input("Enter Buyer Name: ")
    while buyer_name == "":
        print("Buyer Name cannot be empty.")
        buyer_name = input("Enter Buyer Name: ")
    # ask for event name
    event_name = input("Enter Event Name: ")
    while event_name == "":
        print("Event Name cannot be empty.")
        event_name = input("Enter Event Name: ")
    # ask for seat section (V/P)
    while True:
        seat_section = input("Enter Seat Section (V/G): ").upper()
        if seat_section not in("V", "P"):
            print("Please enter either 'V' or 'G'.")
        elif seat_section == "V" and count_VIP(tickets) >= vipCapacity:
            print("VIP tickets are full. Please choose General (G).")
        else:
            break
    # ask for price
    price = float(input("Enter Price: "))
    while price <= 0:
        print("Please enter a positive price.")
        price = float(input("Enter Price: "))
    # ask if paid
    while True:
        paid = input("Enter Paid (Y/N): ").upper()
        if paid in ("Y", "N"):
            break
        else:
            print("Please enter either 'Y' or 'N'.")
    new_ticket = {
        "id": ticket_id,
        "buyer_name": buyer_name,
        "event_name": event_name,
        "seat_section": seat_section,
        "price": price,
        "paid": paid
    }
    tickets.append(new_ticket)
    print("\nTicket added successfully.\n")
    print("------------------------------------")
def display_tickets(tickets):
    if not tickets:
        print("None of Tickets yet !")
    else:
        print("--------------------{ Display all Tickets }--------------------")
        print(f"{'Ticket_ID':<10}{'Buyer_Name':<18}{'Event_Name':<12}{'Seat':<6}{'Price':<12}{'Paid':<12}")
        for ticket in tickets:
            print(f"{ticket['id']:<10}{ticket['buyer_name']:<18}{ticket['event_name']:<12}{ticket['seat_section']:<6}{ticket['price']:<12}{ticket['paid']:<12}")
        print("---------------------------------------------------------------")

;
tickets = []

def main():
    print("----------[ Concert Even Ticketing System Menu ]------------")
    vipCapacity = int(input("Enter maximum VIP capacity: "))
    while vipCapacity < 0:
        print("VIP cannot be less than zero.")
        vipCapacity = int(input("Enter maximum VIP capacity: "))
    choice = 0
    while choice != 9:
        menu()
        choice = int(input("Enter your choice: "))
        match(choice):
            case 1:
                add_ticket(tickets, vipCapacity)
            case 2:
                display_tickets(tickets)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                print("Exiting program...")
            case _:
                print("Invalid choice. Please enter only number 1-9!")


main()
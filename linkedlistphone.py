class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Ticket:
    def __init__(self, seat_number, passenger_name, destination, phone_number):
        self.seat_number = seat_number
        self.passenger_name = passenger_name
        self.destination = destination
        self.phone_number = phone_number

class TicketBookingSystem:
    def __init__(self):
        self.head = None

    def book_ticket(self, seat_number, passenger_name, destination, phone_number):
        new_ticket = Ticket(seat_number, passenger_name, destination, phone_number)
        new_node = Node(new_ticket)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def cancel_ticket(self, seat_number):
        current = self.head
        while current:
            if current.data.seat_number == seat_number:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def display_tickets(self):
        current = self.head
        while current:
            print(f"Seat Number: {current.data.seat_number}, Passenger Name: {current.data.passenger_name}, Destination: {current.data.destination}, Phone Number: {current.data.phone_number}")
            current = current.next

def main():
    ticket_system = TicketBookingSystem()
    while True:
        print("\nMenu:")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Display Tickets")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            seat_number = input("Enter seat number: ")
            passenger_name = input("Enter passenger name: ")
            destination = input("Enter destination: ")
            phone_number = input("Enter phone number: ")
            ticket_system.book_ticket(seat_number, passenger_name, destination, phone_number)
            print("Ticket booked successfully!")
        elif choice == "2":
            seat_number = input("Enter seat number to cancel: ")
            if ticket_system.cancel_ticket(seat_number):
                print("Ticket canceled successfully!")
            else:
                print("Ticket not found.")
        elif choice == "3":
            print("\nTickets booked:")
            ticket_system.display_tickets()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

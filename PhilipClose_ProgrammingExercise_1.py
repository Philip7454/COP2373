# Write an application to pre-sell a limited number of cinema tickets.
# Each buyer can buy up to 4 tickets.
# No more than 20 tickets can be sold total.
# Prompt the user for the desired number of tickets and then display
# the number of remaining tickets after their purchase.
# Repeat until all tickets have been sold.
# Then display the total number of buyers.

# Main function
def main():

    # tickets_remaining is the variable that tells how many
    # tickets are left to sell.
    ticketsRemaining = 20

    # Using a while loop to make sure tickets are being sold
    # until tickets_remaining = 0.
    while ticketsRemaining > 0:

        # Calls the sell_tickets function to sell tickets.
        ticketsRemaining = sell_tickets(ticketsRemaining)
        print(f'There are {ticketsRemaining} tickets left to sell.')

    # This message prints when all tickets have been sold
    # and the program finishes successfully.
    print('Congratulations! All tickets have been sold!')

# sell_tickets is the function that asks the user how many
# tickets they want to buy and calculates how many tickets are
# left afterward.
def sell_tickets(tickets):

    # Using a while True loop with a try/except statement to sell 1 to 4
    # tickets each time and even less if there is less than 4 tickets
    # left to sell.
    while True:
        try:

            # Asks the user how many tickets they are buying.
            ticketsBought = int(input('How many tickets would you like to buy? '))

            # raise errors if a number greater than 4 and less than
            # 1 is entered or if there aren't enough tickets to sell
            # that the person entered.
            if ticketsBought < 1 or ticketsBought > 4:
                raise ValueError
            if ticketsBought > tickets:
                class TicketsBoughtError(Exception):
                    pass
                raise TicketsBoughtError

            # Calculate how many tickets are left after the user
            # buys some and break the loop.
            tickets -= ticketsBought
            break

        # The errors that can be triggered.
        except ValueError:
            print('Please enter a whole number from 1 to 4.')
        except TicketsBoughtError:
            print(f'You can only buy up to {tickets} tickets.')

    # Return the remaining number of tickets back to the main function.
    return tickets

#Call the main function.
main()

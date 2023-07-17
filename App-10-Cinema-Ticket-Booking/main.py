import sqlite3
import random
import string

from fpdf import FPDF


class User:
    """Represents a user that can but a cinema seat
    """

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys the ticket if the card is valid
        :param seat: seat to be bought
        :param card: card where purchase will be made
        :return: message confirming or declining the purchase
        """
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat.seat_id)
                ticket.to_pdf()
                return 'Purchase successful!'
            else:
                return "There was a problem with your card!"
        else:
            return "Seat is taken!"


class Seat:
    """Represents a cinema seat that can be bought by a user
    """

    database = 'cinema.db'

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat
        :return: seat price
        """
        connection = sqlite3.Connection(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id"=?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]
        connection.close()
        return price

    def is_free(self):
        """Check database whether a seat is taken or not
        :return: boolean (represented by int)
        """
        connection = sqlite3.Connection(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id"=?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]
        connection.close()
        return not bool(result)

    def occupy(self):
        """Change the value of taken in the database from 0 to 1 if seat is free
        """
        if self.is_free():
            connection = sqlite3.Connection(self.database)
            connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
            """, [1, self.seat_id])
            connection.commit()
            connection.close()


class Card:
    """Represents a bank card needed to finalize a seat purchase
    """

    database = 'banking.db'

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        """Checks if card is valid and has balance, subtracts price from balance is purchase is successful
        :param price:
        :return: boolean for successful purchase
        """
        connection = sqlite3.Connection(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? AND "cvc"=?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance"=? WHERE "number"=? AND "cvc"=?
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True


class Ticket:
    """Represents a cinema ticket purchased by a user
    """

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = ''.join([random.choice(string.ascii_letters) for _ in range(8)])
        self.seat_number = seat_number

    def to_pdf(self):
        """Creates a ticket PDF
        """
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Your Digital Ticket', border=1, ln=1, align='C')

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Name: ', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Ticket ID', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Price', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Seat Number', border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", ln=1)

        pdf.output('ticket.pdf')


if __name__ == '__main__':
    name = input("Your full name: ")
    seat_id = input("Preferred seat number: ")
    card_type = input("Your card type: ")
    card_number = input("Your card number: ")
    card_cvc = input("Your card cvc: ")
    card_holder = input("Card holder name: ")

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

    print(user.buy(seat=seat, card=card))

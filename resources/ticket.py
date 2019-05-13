from flask_restful import Resource, reqparse
from models.account import PaymentAccount
from models.ticket import Ticket
import random

class TicketResource(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument('ticket_number', type=str, location='args', required=True,
                                 help="ticket_number can't be left blank")
        data = self.parser.parse_args()
        return Ticket.find_by_ticket_number(data.ticket_number).serialize()

    def post(self):
        self.parser.add_argument('firstname',type=str,required=True,help="firstname can't be left blank")
        self.parser.add_argument('lastname',type=str,required=True,help="lastname can't be left blank")
        self.parser.add_argument('email',type=str,required=True,help="email can't be left blank")
        self.parser.add_argument('age',type=int,required=True,help="email can't be left blank")
        self.parser.add_argument('price',type=float,required=True,help="email can't be left blank")
        data = self.parser.parse_args()

        #worst id generator
        while True:
            ticket_number = random.randint(100000, 999999)
            if Ticket.find_by_ticket_number(ticket_number) is None:
                break

        try:
            ticket = Ticket(ticket_number, data.firstname, data.lastname, data.email, data.age, data.price)
            ticket.save_to_db()
            payment_account = PaymentAccount(data.ticket_number, 0)
            payment_account.save_to_db()
            return ticket.serialize()
        except:
            return {'message':"can't create ticket"},500

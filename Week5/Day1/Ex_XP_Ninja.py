class phone_number:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.message_recived = []
        self.message_sent = []
        self.call_history = []
    
    def call (self,other_phone):
        outgoing = f'{self.phone_number} called to {other_phone.phone_number}'
        print(outgoing)
        self.call_history.append(outgoing)
        incoming = f'{other_phone.phone_number} was called from{self.phone_number}'
        other_phone.call_history.append(incoming)

    def send_message (self,other_phone, message):
        sent = {'to': other_phone.phone_number, 
                'content':message}
        recived = {'from': self.phone_number, 
                'content':message}
        self.message_sent.append(sent)
        other_phone.message_recived.append(recived)
    
    def show_outgoing_messages(self):
        for i in self.message_sent:
            print(i)
   
    def show_incoming_messages(self):
        for i in self.message_recived:
            print(i)

    def show_messages_from(self,other):
        for i in self.message_recived:
            if i['from']==other:
                print(i)
            


    def show_call_history (self):
        for i in self.call_history:
            print(i)
        print(self.call_history)

me = phone_number("07777777")
you = phone_number("01111111")
other = phone_number("99999999")

me.call(you)
me.call(other)
me.show_call_history()

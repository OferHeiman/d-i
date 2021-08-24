class Phone():
    call_history = []
    messages=[]

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self,other_phone):
        self.call_history.append(other_phone)
        print(f"{self.phone_number} called {other_phone}")

    def show_call_history(self):
        print(f"The call history is: \n{self.call_history}")

    def send_message(self,to,from1,content):
        self.messages.append({"to":to,'from':from1,'content':content})
    
    def show_outgoing_messages(self):
        print("The outgoing message history is:")
        for dict in self.messages:
            print(dict) if dict.get('from') == self.phone_number else "",

    def show_incoming_messages(self):
        print("The incoming message history is:")
        for dict in self.messages:
            print(dict) if dict.get('to') == self.phone_number else "",

    def show_messages_from(self,phone_number):
        print(f"The messages from {phone_number} are:")
        for dict in self.messages:
            print(dict) if dict.get('from') == phone_number else "",

ofer = Phone('052-516-3295')
print(f"My phone number is: {ofer.phone_number}")
ofer.call("052-246-5231")
ofer.call("054-916-3840")
ofer.show_call_history()
ofer.send_message('052-246-5231','052-516-3295',"what's up")
ofer.send_message('052-516-3295','052-246-5231',"hello")
ofer.send_message('052-516-3295','050-143-6229',"hey there")
ofer.send_message('052-516-3295','052-246-5231',"how's it going")
print(f"The message history is: \n{ofer.messages}")
ofer.show_outgoing_messages()
ofer.show_incoming_messages()
ofer.show_messages_from('052-246-5231')
ofer.show_messages_from('050-143-6229')
import termii_switch
import termii_insight

class Client:
    """
    Creates a termi client using the api_key
    ...

    Attributes:
    api_key: str 
        The termii developer API Key to create a client from.
    """
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_sender_ids(self):
        """
        A method to request new termii sender ID.
        """
        response = termii_switch.get_sender_ids(self.api_key)
        return response
    
    def request_sender_id(self, sender_id, usecase, company):
        """
        A method to request new termii sender ID.

        Params:
        sender_id: str
            The name of the new sender_id to create
        usecase: str
            The usecase of the new sender_id. Must be at least 20 characters
        company: str
            The name of the company associated with this sender_id
        """

        response = termii_switch.request_new_sender_id(self.api_key, sender_id, usecase, company)
        return response
    
    def send_message(self, number_to, sender_id, message, message_type, channel, media_dict):
        """
        A method to send a message using the termii API.

        Params:
        number_to: str
            The phone number the message should be sent to in international format. '+' should be excluded
        sender_id: str
            The sender id this message should be sent from and identify with
        message: str
            The message to be sent.
        message_type: str
            The type of message to be sent. Should be 'plain'
        channel: str
            The channel this message should be sent with. Can be 'dnd', 'whatsapp' or 'generic'
        media_dict: dict
            A dictionary containing the options for media if applicable. Should contain 'url' and 'caption' keys. Pass an empty dictionary if not applicable
        """
        response = termii_switch.post_message(self.api_key, number_to, sender_id, message, message_type, channel, media_dict)
        return response

    def send_bulk_sms(self, numbers_to, sender_id, message, message_type, channel):
        """
        A method to send bulk sms messages using the termii api.

        Params:
        numbers_to: str
            An array containing the phone numbers the message should be sent to in international format. '+' should be excluded
        sender_id: str
            The sender id this message should be sent from and identify with
        message: str
            The message to be sent.
        message_type: str
            The type of message to be sent. Should be 'plain'
        channel: str
            The channel this message should be sent with. Can be 'dnd', 'whatsapp' or 'generic'
        """

        response = termii_switch.post_message_bulk(self.api_key, numbers_to, sender_id, message, message_type, channel)
        return response

    def send_message_with_autogenerated_number(self, number_to, message):
        """
        A method to send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.

        Params:
        number_to: str
            The phone number the message should be sent to in international format. '+' should be excluded
        message: str
            The message to be sent.
        """

        response = termii_switch.number_message_send(self.api_key, number_to, message)
        return response

    def send_device_template(self, phone_number, device_id, template_id, data):
        """
        A method to set a device template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.

        Params:
        phone_number: str
            The destination phone number. Phone number must be in the international format without '+'
        device_id: str
            Represents the Device ID for Whatsapp. It can be Alphanumeric. It should be passed when the message is sent via whatsapp (It can be found on the manage device page on your Termii dashboard)
        template_id: str
            The ID of the template used
        data: dict
            Represents an object of key: value pair. The keys for the data object can be found on the device subscription page on your dashboard.
        """

        response = termii_switch.template_setter(self.api_key, phone_number, device_id, template_id, data)
        return response

    def fetch_phonebooks(self):
        """
        A method to get all the phonebooks associated to a termii client
        """
        
        response = termii_switch.get_phonebooks(self.api_key)
        return response

    def create_phonebook(self, description, phonebook_name):
        """
        A method to create a phonebook using the termii API

        Params:
        description: str
            A description of the contacts stored in the phonebook
        phonebook_name: str
            The name of the phonebook
        """
        response = termii_switch.make_phonebook(self.api_key, description, phonebook_name)
        return response
    
    def update_phonebook(self, phonebook_id, phonebook_name, phone_description):
        """
        A method to create a phonebook using the termii API

        Params:
        phonebook_id: str
            The id of the phonebook to be updated
        phonebook_name: str
            The new name of the phonebook
        phonebook_description: str
            The new description of the phonebook
        """

        response = termii_switch.patch_phonebook(self.api_key, phonebook_id, phonebook_name, phone_description)
        return response

    def delete_phonebook(self, phonebook_id):
        """
        A method to delete a phonebook using the termii API

        Params:
        phonebook_id: str
            The id of the phonebook to be updated
        """

        response = termii_switch.remove_phonebook(self.api_key, phonebook_id)
        return response
    
    def fetch_contacts(self, phonebook_id):
        """
        A method to get all the contacts associated to a termii phonebook

        Params:
        phonebook_id: str
            The id of the phonebook
        """
        
        response = termii_switch.get_contacts_from_phonebook(self.api_key, phonebook_id)
        return response
    
    def add_new_contact(self, phone_number, phonebook_id, options):
        """
        A method to add a single contact to a phonebook using the termii API

        Params:
        phone_number: str
            Phone number of the contact without international format.
        phonebook_id: str
            The id of the phonebook
        options: dict
            A dictionary containing certain options such as 'country_code', 'email_address', 'first_name', 'last_name' and 'company' which are all strings. An empty dictionary should be passed if there are no options.
        """

        response = termii_switch.add_contact(self.api_key, phone_number, phonebook_id, options)
        return response
    
    def add_contacts(self, contact_file, country_code, extension, phonebook_id):
        """
        A method to add contacts to a phonebook using the termii API

        Params:
        contact_file: str
            File containing the list of contacts you want to add to your phonebook. Supported files include : 'txt', 'xlsx', and 'csv'.
        country_code: str
            Represents short numeric geographical codes developed to represent countries (Example: 234 ).
        extension: str
            The extension of the contact file: (Example: 'text/csv')
        phonebook_id: str
            The id of the phonebook
        """

        response = termii_switch.add_many_contacts(self.api_key, contact_file, country_code, extension, phonebook_id)
        return response

    def delete_contact(self, contact_id):
        """
        A method to delete contacts from a phonebook using the termii API

        Params:
        api_key: str
            The API key for a certain termii account
        contact_id: str
            The id of the contact to be deleted
        """

        response = termii_switch.delete_one_contact(self.api_key, contact_id)
    
    def send_campaign(self, country_code, sender_id, message, channel, message_type, phonebook_id, campaign_type, **schedule):
        """
        A method to send campaigns using the termii API

        Params:
        country_code: str
            Represents short numeric geographical codes developed to represent countries (Example: 234 ) .
        sender_id: str
            Represents the ID of the sender which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters
        message: str
            Text of a message that would be sent to the destination phone number
        channel: str
            This is the route through which the message is sent. It is either dnd, whatsapp, or generic
        message_type: str
            The type of message that is sent, which is a plain message.
        phonebook_id: str
            ID of the phonebook selected    
        campaign_type: str
            Represents type of campaign
        schedule_sms_status: str| Optional
            To send a scheduled campaign, pass 'scheduled' as the value
        schedule_time: str| Optional
            The time to send scheduled campaign. This is required if scheduled_sm_status is 'scheduled'. In the format '30-06-2021 6:00'
        """

        response = termii_switch.make_campaign(self.api_key, country_code, sender_id, message, channel, message_type, phonebook_id, campaign_type, **schedule)
        return response
    
    def fetch_campaigns(self):
        """
        A method to get the all campaigns associated with a client
        """

        response = termii_switch.get_campaigns(self.api_key)
        return response
    
    def fetch_campaign_history(self, campaign_id):
        """
        A method to get the history of a certain campaign

        Params:
        campaign_id: str
            The ID of the campaign history to be fetched
        """

        response = termii_switch.get_campaign_history(self.api_key, campaign_id)
        return response
    
    def get_balance(self):
        """
        A method to check a client's termii balance
        """

        response = termii_insight.check_balance()
        return response
    
    def search_number(self, phone_number):
        """
        A method to verify phone numbers and automatically detect their status

        Params: 
        phone_number: str
            Represents the phone number to be verified. Phone number must be in the international format without the '+'
        """

        response = termii_insight.check_number(phone_number)
        return response

    def search_number_status(self, phone_number, country_code):
        """
        A method to detect if a number is fake or has ported to a new network.

        Params: 
        api_key: str
            The termii api_key associated with the client
        phone_number: str
            Represents the phone number to be verified. Phone number must be in the international format without the '+'
        country_code: str
            Represents short alphabetic codes developed to represent countries (Example: NG ).
        """

        response = termii_insight.get_number_status(self.api_key, phone_number, country_code)
        return response

    def fetch_history(self):
        """
        A method that returns reports for messages sent across the sms, voice & whatsapp channels.
        """

        response = termii_insight.get_full_history(self.api_key)
        return response


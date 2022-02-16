from urllib import response
import termii_switch
import termii_token
import termii_insight

class Client:
    """
    Creates a termi client using the api_key
    ...

    Attributes:
    api_key: str 
        The termii developer API Key to create a client from.

    Methods:
    fetch_sender_ids: A method to request new termii sender ID.
    request_sender_id: A method to request new termii sender ID.
    send_message: A method to send a message using the termii API.
    send_bulk_sms: A method to send bulk sms messages using the termii API.
    send_message_with_autogenerated_number: A method to send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.
    send_device_template: A method to set a device template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.
    fetch_phonebooks: A method to get all the phonebooks associated to a termii client
    create_phonebook: A method to create a phonebook using the termii API
    update_phonebook: A method to update phonebook using the termii API
    delete_phonebook: A method to delete a phonebook using the termii API
    fetch_contacts: A method to get all the contacts associated to a termii phonebook
    add_new_contact: A method to add a single contact to a phonebook using the termii API
    add_contacts: A method to add contacts to a phonebook using the termii API
    delete_contact: A method to delete contacts from a phonebook using the termii API
    send_campaign: A method to send campaigns using the termii API
    fetch_campaigns: A method to get the all campaigns associated with a client
    fetch_campaign_history: A method to get the history of a certain campaign
    get_balance: A method to check a client's termii balance
    search_number: A method to verify phone numbers and automatically detect their status
    search_number_status: A method to detect if a number is fake or has ported to a new network.
    fetch_history: A method that returns reports for messages sent across the sms, voice & whatsapp channels.
    send_token:  A method that allows businesses trigger one-time-passwords(OTP) across any available messaging channel on Termii.
    voice_token: A method that enables you to generate and trigger one-time-passwords via a voice channel to a phone number.
    voice_call: A method that enables you to send messages from your application through a voice channel to a client's phone number.
    verify_token:  A method that checks tokens sent to customers and returns a response confirming the status of the token.
    in_app_token: A method that returns OTP code in JSON fromat which can be used in any web or mobile app.
    """
    def __init__(self, api_key):
        self.api_key = api_key

    """ START OF METHODS FOR SWITCH"""
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
        A method to send bulk sms messages using the termii API.

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
        A method to update a phonebook using the termii API

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
    
    def add_new_contact(self, phone_number, phonebook_id, country_code, options):
        """
        A method to add a single contact to a phonebook using the termii API

        Params:
        phone_number: str
            Phone number of the contact without international format.
        phonebook_id: str
            The id of the phonebook
        country_code: str
            The country code of the number to be added
        options: dict
            A dictionary containing certain options such as 'email_address', 'first_name', 'last_name' and 'company' which are all strings. An empty dictionary should be passed if there are no options.
        """

        response = termii_switch.add_contact(self.api_key, phone_number, phonebook_id, country_code, options)
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
        return response
    
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
    """ END OF METHODS FOR SWITCH """
    
    """ START OF METHODS FOR INSIGHT """
    def get_balance(self):
        """
        A method to check a client's termii balance
        """

        response = termii_insight.check_balance(self.api_key)
        return response
    
    def search_number(self, phone_number):
        """
        A method to verify phone numbers and automatically detect their status

        Params: 
        phone_number: str
            Represents the phone number to be verified. Phone number must be in the international format without the '+'
        """

        response = termii_insight.check_number(self.api_key, phone_number)
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
    """ END OF METHODS FOR INSIGHT """


    """ START OF METHODS FOR TOKEN """
    
    def send_token(self, message_type, phone_number, 
        sender_id, channel, pin_attempts, pin_time_to_live,
        pin_length, pin_placeholder, message_text):

        """
        A method that allows businesses trigger one-time-passwords(OTP)
        across any available messaging channel on Termii. The OTP are created
        generated randomly and there's an optionto set an expiry time.
        """

        response = termii_token.send_new_token(self.api_key, message_type, 
        phone_number, sender_id, channel, pin_attempts, pin_time_to_live,
        pin_length, pin_placeholder, message_text)
        return response
    
    def voice_token(self, phone_number, pin_attempts, pin_time_to_live, pin_length):
        """
        A method that enables you to generate and trigger one-time-passwords
        via a voice channel to a phone number. OTPs are generated and sent to
        phone numbers and can only be verified using Verify Token function.

        Parameters:
        api_key : string
            API key for Termii account.
        phone_number : integer
            The destination number of the client receiving the voice token.
            Number must be in international format.
        pin_attempts : NUMERIC / ALPHANUMERIC
            PIN code that is generated and sent with the OTP message.
            Has a minimum of one attempt.
        pin_time_to_live : integer
            Represents time of pin validation before expiry.
            Time is in minutes and has a minimum of 0 and maximum of 60.
        pin_length : integer
            Length of PIN code. Has a minimum of 4 and maximum of 8.
    """
        response = termii_token.send_voice_token(self.api_key, phone_number, pin_attempts, pin_time_to_live, pin_length)
        return response

    def voice_call(self, phone_number, code, pin_attempts, pin_time_to_live, pin_length):
        """
        A method that enables you to send messages from your application through
        a voice channel to a client's phone number. Only one-time-passwords are
        allowed for now and they cannot be verified via the Verify Token Function

        Parameters:
        api_key : string
            API key for Termii account.
        phone_number : integer
            The destination number of the client receiving the voice token.
            Number must be in international format.
        code : numeric
            The code the client receives. It has to be numeric and length must
            be between 4 and 8 digits.
        pin_attempts : integer
            Represents the number of times the PIN can be attempted before
            expiration. Has a minimum of one attempt.
        pin_time_to_live : integer
            Represents how long the pin is valid before expiration. The time is
            in minutes. The minimum time value is 0 and maximum is 60.
        pin_length : integer
            Length of the pin code. Has a minimum of 4 and maximum of 8.
        """
        response = termii_token.make_voice_call(self.api_key, phone_number, code, pin_attempts, pin_time_to_live, pin_length)
        return response
    
    def verify_token(self, pin_id, pin):
        """
         A method that checks tokens sent to customers and returns a response
        confirming the status of the token. A token can either be confirmed
        as verified or expired based on the timer set for the token.

        Parameters:
        api_key : string
            API key for Termii account
        pin_id : string
            ID of the pin sent (Example: "c8dcd048-5e7f-4347-8c89-4470c3af0b")
        pin : string
            The pin code (Example: "195558")
        """
        response = termii_token.verify_sent_token(self.api_key, pin_id, pin)
        return response
    
    def in_app_token(self, phone_number, pin_attempts, pin_time_to_live, pin_length):
        """
        A method that returns OTP code in JSON fromat which can be used in any
        web or mobile app. Tokens are numeric or alpha-numeric codes generated
        to authenticate login requests and verify customer transactions.

        Parameters:
        api_key : string
            API key for Termii account
        pin_type : NUMERIC / ALPHANUMERIC
            Type of pin code that will be generated and sent as part of the OTP
            message. Can be set to numeric or alphanumeric.
        phone_number : string
            Represents the destination phone number. Phone number must be in
            international format.
        pin_attempts : integer
            Represents the number of times the PIN can be attempted before
            expiration. Has a minimum of one attempt.
        pin_time_to_live : integer
            Represents how long the pin is valid before expiration. The time is
            in minutes. The minimum time value is 0 and maximum is 60.
        pin_length : integer
            Length of the pin code. Has a minimum of 4 and maximum of 8.
        """
        
        response = termii_token.send_token_in_app(self.api_key, phone_number,
        pin_attempts, pin_time_to_live, pin_length)
        return response
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import SlotSet, AllSlotsReset, ConversationPaused, ConversationResumed
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class AllSlotsResetDemo(Action):
	def name(self):
		return 'action_slot_reset_demo'
	def run(self, dispatcher, tracker, domain):
			return[AllSlotsReset()]



class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "ACTION_DEFAULT_FALLBACK_NAME"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="my_custom_fallback_template")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]




class ActionSubmitData(Action):

    def name(self) -> Text:
        return "action_submit_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            # user_name = tracker.get_slot("user_name")
            crime_date = tracker.get_slot("crime_date")
            crime_time = tracker.get_slot("crime_time")
            # report_date = tracker.get_slot("report_date")
            # report_time = tracker.get_slot("report_time")
            crime_location = tracker.get_slot("crime_location")
            suspected_people = tracker.get_slot("suspected_people")
            sname = tracker.get_slot("sname")
            cname = tracker.get_slot("cname")
            crime_type = tracker.get_slot("crime_type")
            stolen_things = tracker.get_slot("stolen_things")
            stolen_amount = tracker.get_slot("stolen_amount")
            injury_occured = tracker.get_slot("injury_occured")
            people_with = tracker.get_slot("people_with")
            vehicle_type = tracker.get_slot("vehicle_type")
            number_people_died = tracker.get_slot("number_people_died")
            person_location = tracker.get_slot("person_location")
            kidnapper_call = tracker.get_slot("kidnapper_call")
            if kidnapper_call == None:
                kidnapper_call = "No contact"            
            call_details = tracker.get_slot("call_details")
            robbery_details = tracker.get_slot("robbery_details")
            accident_details = tracker.get_slot("accident_details")
            

            """
            msg = "Data [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}] is to be sent to the database...!!!".format(
                     crime_date, crime_time, crime_location, suspected_people, stolen_things
                    , stolen_amount, sname, cname, crime_type, injury_occured, people_with, vehicle_type
                    , number_people_died, person_location, kidnapper_call, call_details, robbery_details, accident_details)
"""
            msg = "Required data has been captured..."
            dispatcher.utter_message(text=msg)

            return []


class ValidateBasicUserDetailsForm(FormValidationAction):
   

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "validate_basic_user_details_form"
    # validate user answers
    user_state= None

    @staticmethod
    def state_db() -> Dict[str, List]:
        """Database of multiple choice answers"""
        return [ "gujarat","maharastra","rajasthan"]

    def validate_sname(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> Dict[Text, Any]:
            """Validate user input."""

            if value.lower() in self.state_db():
                # validation succeeded, set the value of the slot to
                # user-provided value
                ValidateBasicUserDetailsForm.user_state=value.lower()
                
                return {"sname": value.lower()}
            else:
                dispatcher.utter_template("utter_wrong_sname", tracker)
                ValidateBasicUserDetailsForm.user_state=None

                return {"sname": None}
    
    @staticmethod
    def city_db() -> Dict[str, List]:
                """Database of multiple choice answers"""
                # sname= tracker.get_slot("sname")
                if  ValidateBasicUserDetailsForm.user_state == "gujarat":
                    return [ "surat","rajkot"]
                elif ValidateBasicUserDetailsForm.user_state == "maharastra":
                    return [ "mumbai","pune"]
       
    def validate_cname(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> Dict[Text, Any]:
            """Validate user input."""
            # sname= tracker.get_slot("sname")

            if value.lower() in self.city_db():
                # validation succeeded, set the value of the slot to
                # user-provided value
                return {"cname": value.lower()}
            else:
                dispatcher.utter_template("utter_wrong_cname", tracker)
                return {"cname": None}

class CallDeatilsForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "kidapping_details_form"
      
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return["call_details"]
    def slot_mappings(self) -> Dict[Text,Union[Dict,List[Dict]]]:
        return{

            "call_details": self.from_text()
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        return []


class RobberyDatilsForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "robbery_details_form"
      
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return["robbery_details"]
    def slot_mappings(self) -> Dict[Text,Union[Dict,List[Dict]]]:
        return{

            "robbery_details": self.from_text()
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        return []

class AccidentDeatilsForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "accident_details_form"
      
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return["accident_details"]
    def slot_mappings(self) -> Dict[Text,Union[Dict,List[Dict]]]:
        return{

            "accident_details": self.from_text()
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        return []
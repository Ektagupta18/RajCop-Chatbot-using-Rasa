# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionArrestedPersons(Action):
    def name(self) -> Text:
        # Name of the custom action
        return "action_arrested_persons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Add logic here to fetch or generate information about arrested persons
        arrested_persons = [
            {"name": "John Doe", "crime": "Theft", "arrest_date": "2024-12-01"},
            {"name": "Jane Smith", "crime": "Fraud", "arrest_date": "2024-12-03"}
        ]

        # Format the response
        if arrested_persons:
            response = "Here is the list of arrested persons:\n"
            for person in arrested_persons:
                response += f"- {person['name']} (Crime: {person['crime']}, Arrested on: {person['arrest_date']})\n"
        else:
            response = "Currently, no persons are under arrest."

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []

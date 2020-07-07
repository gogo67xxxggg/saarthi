# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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

class ActionDomain(Action):

	def name(self) -> Text:
		return "action_domain_service"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		try:
			prediction = tracker.latest_message
			entity_value = prediction['entities'][0]['value']
			resp = "I do provide service in "+entity_value+" domain."
			dispatcher.utter_message(text=resp)
		except:
			dispatcher.utter_message(text="Hii, I work in numerous domains, ranging from sales, IT, finance, medical, food delivery, telecom, etc")

		return []

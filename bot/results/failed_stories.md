## happy path 1 (/tmp/tmpm8fbsf_v/72a25be5f27b475f847cd2d63ea78d17_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: appreciate: amazing -->
    - utter_happy   <!-- predicted: utter_appreciate -->


## happy path 2 (/tmp/tmpm8fbsf_v/72a25be5f27b475f847cd2d63ea78d17_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: appreciate: amazing -->
    - utter_happy   <!-- predicted: utter_appreciate -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (/tmp/tmpm8fbsf_v/72a25be5f27b475f847cd2d63ea78d17_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_appreciate -->


## sad path 2 (/tmp/tmpm8fbsf_v/72a25be5f27b475f847cd2d63ea78d17_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye


## sad path 3 (/tmp/tmpm8fbsf_v/72a25be5f27b475f847cd2d63ea78d17_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: affirm: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_appreciate -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye



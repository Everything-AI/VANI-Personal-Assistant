# VANI, the Personal Assistant

VANI is an innovative, inexpensive, and reliable Virtual Assistant which was developed to perform many of the tasks commonly performed by a traditional secretary. It can thus, reduce the human efforts and hassle by fulfilling various tasks all at one place. Advance features of VANI also includes the ability to chat with humans, like humans!

## Project Deliverables

The problems faced by other Virtual Assistants were that they took a huge amount to data and computational power to train to give off the responses. However with VANI, the problem was solved a bit as it was trained using much lesser data and the responses which it generated were still considerate. 

## Model Description

VANI was developed using Machine Learning abstractions, so the main aim was not just to instigate a virtual assistant but, the model itself was of prime importance which lead to its innumerous applications. Furthermore, the model used was sequence-to-sequence, written from scratch, which made all the  difference. Additionally, its application was not at all domain specific as the model which was generated can be applied to more problem statements like machine translation, text summarization, etc. 

## Trigger Actions

The Assistant can behave and talk just like any other personal assistant as it is capable of chatting with the user through texts and messgages. Nonetheless, it also responds to the trigger actions, which may include:

- Searching anything on Google (Say Anything followed by **Search..**)
- Telling some jokes (activated by **Tell Me a Joke**)
- Playing Media on Youtube (Triggers on saying anything followed by **Play..**)
- Displaying weather forcast for any place (**Weather Forcast at/in..**)
- Opening any other site on browser

The model was made not to store any data on database so it is better thamn its rival counterparts.

## Requirement Specifications

1. Computer System to run application on, with dependencies:
   - Python 3.5
   - Tensorflow 0.12.1
   - Flask
   - pyttsx3
   - speech_recognition
2. Webbrowser (chrome driver in the repo)
3. Internet Connection (to perform searches)

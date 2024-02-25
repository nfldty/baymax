import cohere
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
# Now you can access environment variables using `os.getenv()`
from cohere.responses.classify import Example
co = cohere.Client(os.getenv("COHERE_API_KEY"))
examples = [
    Example("thank you for your help.", "Yes"),
    Example("Thank you", "Yes"),
    Example("I'll follow up with my primary care physician, goodbye!", "Yes"),
    Example("I have to go now, I'll come back if I have more questions.", "Yes"),
    Example("Thank you for the information, I'll take care of myself.", "Yes"),
    Example("I'll take the prescribed medication as instructed, goodbye.", "Yes"),
    Example("I'll let you know if I need further assistance, goodbye.", "Yes"),
    Example("Thanks for your time, I'll consult my doctor for further advice.", "Yes"),
    Example("I appreciate your help, I'll let you know how it goes.", "Yes"),
    Example("I'll end the conversation here, take care.", "Yes"),
    Example("I'll get back to you if I need more help, goodbye.", "Yes"),
    Example("Thanks for the diagnosis. Could you clarify the dosage instructions for me?", "No"),
    Example("What are the potential side effects of this medication?", "No"),
    Example("Thank you. Can you recommend any lifestyle changes for managing this condition?", "No"),
    Example("I have a question about my diet, can you provide some guidance?", "No"),
    Example("Is it safe to combine this medication with herbal supplements?", "No"),
    Example("Can you explain how this treatment works in more detail?", "No"),
    Example("I'm not sure I understand the risks associated with this procedure.", "No"),
    Example("What are the alternatives to surgery for treating this condition?", "No"),
    Example("Thanks. But I need more information before making a decision, can you help?", "No"),
    Example("I'm considering a second opinion, do you have any recommendations?", "No")
    ]


def exit(text):
    """
    Returns True if user wants to exit the program. Otherwise, False.
    """
    response = co.classify(
    inputs= [text],
    examples=examples,
    )
    prediction = response.classifications[0]
    #print(prediction.confidence)
    if prediction.prediction == "Yes" and prediction.confidence > 0.99:
        return True
    return False
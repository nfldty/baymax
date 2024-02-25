import cohere
from cohere.responses.classify import Example
import classification
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
# Now you can access environment variables using `os.getenv()`
from cohere.responses.classify import Example
co = cohere.Client(os.getenv("COHERE_API_KEY"))
def reply(text):
    response = co.chat(
    model='6c1924a9-b363-4890-9e5e-6e72b24dfc5f-ft',
    message="You are a medical assistant. Your role is to provide assistance and guidance to users regarding their health concerns. If the user's message is unclear, ask them to provide more details about their symptoms. Remember to keep the conversation flowing smoothly and to take into account what the user has previously shared. Here is the message from the user: {text}")
    #documents = [{"Disease" :"Panic disorder", "Symptom" :"['Anxiety and nervousness', 'Depression', 'Shortness of breath', 'Depressive or psychotic symptoms', 'Sharp chest pain', 'Dizziness', 'Insomnia', 'Abnormal involuntary movements', 'Chest tightness', 'Palpitations', 'Irregular heartbeat', 'Breathing fast']","Medical Tests":"['Psychotherapy', 'Mental health counseling', 'Electrocardiogram', 'Depression screen (Depression screening)', 'Toxicology screen', 'Psychological and psychiatric evaluation and therapy']", "Medication" : "['Lorazepam', 'Alprazolam (Xanax)', 'Clonazepam', 'Paroxetine (Paxil)', 'Venlafaxine (Effexor)', 'Mirtazapine', 'Buspirone (Buspar)', 'Fluvoxamine (Luvox)', 'Imipramine', 'Desvenlafaxine (Pristiq)', 'Clomipramine', 'Acamprosate (Campral)']"}])
    return response.text

text = "I have gerd"
print(reply(text))
print(classification.exit(text))

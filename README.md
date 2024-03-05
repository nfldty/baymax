## Devpost
[https://devpost.com/software/baymax-p8fv13]

## Inspiration
Reflecting on my own experience of spending 10 agonizing hours waiting to see a doctor for what I feared was a significant eye problem, only to receive a simple solution of warm water compresses. Moreover, it's not just me; countless Canadians share similar grievances about long wait times and difficulty accessing healthcare services. I realized the urgent need for a better way. No one should have to endure such prolonged waits for basic care, especially when facing uncertainty and fear. That memory fuels our team's mission to transform healthcare accessibility in Canada. Together, we're committed to sparing others from similar frustrations by providing efficient, personalized diagnoses through our virtual doctor assistant.
## What it does
Our virtual doctor assistants aren't just tools—they're your trusted companions on the path to better health. Engage in conversations with avatars that look, feel, and think like real human doctor assistants, providing you with personalized medical guidance in a way that's intuitive and trustworthy. 

Of course, one might consider searching online for medical information, but how reliable is it? That's why we're pioneering a solution that goes beyond mere internet searches. Our virtual doctor assistant, BayMax, utilizes AI fine-tuned through 100,000 real conversations between doctors and patients, coupled with a comprehensive database sourced from reputable medical references like Wikipedia. This ensures unparalleled accuracy in diagnosing conditions, analyzing symptoms, and recommending medications. With our platform, you can trust that the guidance you receive is backed by a wealth of medical expertise, making healthcare decisions with confidence and peace of mind.
## How we built it
For the language model, we fine-tuned Cohere's chat model with 100,000 real conversations between doctors and patients from online medical consultation platform which is available to use online. Moreover, we use Cohere's rerank to select the most relevant document from our medical database, and send it alongside the user's query to improve the accuracy. We also use Cohere's Generate and classify for name entity recognition and user's intention classifier, ensuring a personalized and natural conversation. 

To animate and enable the avatar to speak, we convert the chatbot's responses using Google Cloud Text-to-Speech and send them to NVIDIA Audio2Face via the GRPC protocol. Subsequently, we stream the animated facial weights and audio into Unreal Engine through NVIDIA ACE Cloud. These animated facial weights are then mapped to actor that we have created in Unreal Engine and rendered accordingly.
## Challenges we ran into
One significant challenge we encountered was the compatibility issue between the NVIDIA API and our team's hardware setup. The NVIDIA API could only run on Windows operating systems, while many team members used MacBooks. This posed a hurdle that required us to find creative workarounds to ensure everyone could contribute effectively.

Additionally, crafting lifelike avatars presented its own set of difficulties. Making the avatars resemble humans convincingly was a complex task that required careful attention to detail and artistic skill.

Furthermore, mastering the Cohere API for natural language processing posed another challenge. For many of us, including myself, it was our first time working with this technology, requiring us to learn and adapt quickly.

Despite these obstacles, our team remained committed to delivering a high-quality product. Through collaboration and perseverance, we successfully navigated these challenges and emerged stronger as a result.
## Accomplishments that we're proud of
We've reached some big achievements that stand out on our journey. One of them is creating a working avatar. It was a lot of work, but seeing our virtual assistant come to life was amazing. It makes talking to it feel more real and fun.

Also, our team member figured out how to use the Cohere API for the first time. It was a big deal because it helps our virtual assistant understand what people say and give better responses. It's like teaching our assistant to talk like a real person.

But what makes us happiest is that our idea turns into something real and useful. We believe it can make a difference in how people get healthcare help. These accomplishments show how far we've come and make us excited to keep going, dreaming, and making things even better.
## What we learned
In our journey, we delved into cutting-edge technology, mastering the Cohere API for natural language processing and real data utilization. Additionally, we explored avatar technology using the NVIDIA API, bringing lifelike avatars to our virtual assistants. Beyond tech, we discovered the value of collaboration, resilience, and the relentless pursuit of excellence. Moreover, we recognized the paramount importance of user experience and trust-building in the realm of healthcare technology. As we meticulously crafted lifelike avatars and fine-tuned conversational abilities, we understood that beyond the technological advancements, fostering trust and engagement with users is essential. With each lesson learned, we're propelled closer to reshaping healthcare and making a tangible impact on the world.
## What's next for BayMax
BayMax is gearing up to revolutionize the way we approach wellness. Our roadmap includes expanding BayMax's capabilities to offer even more personalized and comprehensive healthcare solutions.

We're investing in further refining BayMax's AI algorithms to enhance diagnostic accuracy and efficiency. Additionally, we're exploring partnerships with healthcare providers to integrate BayMax into existing systems, making access to virtual healthcare more seamless and widespread.

But we're not stopping there. We're also exploring avenues to enhance BayMax's user experience, from improving avatar interactions to implementing new features based on user feedback.

Furthermore, we envision BayMax playing a pivotal role at the front desk of hospitals, where it can assist in patient triage by quickly assessing symptoms and determining the appropriate care pathway. With BayMax's assistance, patients can be efficiently sorted, ensuring they receive timely and appropriate care, while also alleviating strain on healthcare staff.

With BayMax, the future of healthcare is bright, and we're committed to leading the charge toward a healthier world. Stay tuned for exciting updates as we continue to push the boundaries of innovation!

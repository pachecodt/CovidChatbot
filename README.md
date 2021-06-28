# Covid FAQ Chatbot
#### Video Demo:
#### Description: This project aims to create a bot to help people with FAQ (Frequently Asked Questions) about COVID-19. Information taken from WHO
  
## Topics
* [Information](#information)
* [Requirements](#requirements)
* [How to use](#how-to-use)
* [Run](#run)
* [Possible improvements](#possible-improvements)
* [Contributing](#contributing)


### Information
This project should be used to answer questions regarding COVID.
Information base used: WHO(World Health Organization).

Many people do not have up-to-date information about covid.In this case you can chat with this bot as if you would do to a close friend.
You can see a sample conversation in the image below:

![image](https://user-images.githubusercontent.com/18306550/123686425-b3750380-d847-11eb-87eb-e2d45ada5f0e.png)

Tech: 

- Python
- Keras
- nltk
- numpy
- other small libraries or packages


### Requirements
>```
>pip install -r requirements.txt
>```

You will need to have a server listening for information on the /bot route.

In this project I recommend twilio taht is already in specifications. You cancreate an free account [here](https://www.twilio.com/).

After that configure the message settings to the router in the project and than you can use it for SMS or whasapp messages.

The same principle applies to Chatbot with discord, slack or any other.
  
### How to use
  
Local: After installing the dependencies, you can download [Ngrok](https://ngrok.com/download). This way you can exposes your local servers for the world.
Use the ngrok link for your bot.
Example:
>```
>ngrok http 5000
>```

  
### Run

If you have change the model. Before runing your Chat.py, first, train the model. You can train it whenever you want after updating intent.json file.

Train:
>```
>python train_chatbot.py
>```

Than run the application 
>```
>python bot.py
>```

### Possible improvements

As all applications this one need to be improved. Possible improvements:

- Continue to improve the model
- Add answer to number of daily cases.
- Add number of people vaccinated.
  
### Contributing
------------

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

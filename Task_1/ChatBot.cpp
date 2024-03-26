#include <iostream>
#include <string>
#include <algorithm>
#include <regex>
using namespace std;

regex byeRegex("bye|goodbye|go away|good bye|see you|don't want to talk", regex_constants::icase);
// Function to get response based on user input
string getResponse(const string &userInput)
{
    // Predefined patterns and responses
    regex hiRegex("hi|hello|hey|yup|listen|start|let's start|let start|Hi there|Good morning|Good afternoon|Good evening", regex_constants::icase);
    regex howAreYouRegex("how are you?|how do you do", regex_constants::icase);
    regex whoAreYouRegex("who are you?|who are you|introduce|introduce yourself|tell me about yourself|tell me yourself|Are you a bot?", regex_constants::icase);
    regex goodNightRegex("good night|feel sleepy", regex_constants::icase);
    regex helpRegex("Can you help me?|I need assistance", regex_constants::icase);
    regex nameRegex("What's your name?|whats your name?|what is your name", regex_constants::icase);
    regex myWorkRegex("What can you do?|What services do you offer?", regex_constants::icase);

    // Pattern matching and response selection
    if (regex_search(userInput, hiRegex))
    {
        return "Hello! How can I assist you?";
    }
    else if (regex_search(userInput, howAreYouRegex))
    {
        return "I'm just a chatbot, but thanks for asking!";
    }
    else if (regex_search(userInput, nameRegex))
    {
        return "I'm just a chatbot, I don't have any name but my creater Mohd Yusuf call me ryzen";
    }
    else if (regex_search(userInput, myWorkRegex))
    {
        return "I'm a chatbot. I can chat with you.";
    }
    else if (regex_search(userInput, helpRegex))
    {
        return "Of course, I'd be happy to help! What specifically do you need assistance with?";
    }
    else if (regex_search(userInput, whoAreYouRegex))
    {
        return "I'm your trusty chatbot, Think of me as your digital sidekick, ready to engage in conversation, and \nhelp you navigate the vast expanse of the internet. So, what can I do for you today?";
    }
    else if (regex_search(userInput, goodNightRegex))
    {
        return "Okay no problem! You can sleep now. have sleep peacefully!";
    }
    else if (regex_search(userInput, byeRegex))
    {
        return "Goodbye! Have a great day!";
    }
    else
    {
        return "I'm sorry, I didn't understand that.";
    }
}

int main()
{
    cout << "Welcome to the ChatBot!\n";
    cout << "You can start chatting. Or Type 'bye' to exit.\n";

    string userInput;
    while (true)
    {
        cout << "You: ";
        getline(cin, userInput);
        // transform(userInput.begin(), userInput.end(), userInput.begin(), ::tolower); // Convert input to lowercase
        if (regex_search(userInput, byeRegex))
        {
            cout << "Chatbot: Goodbye! Have a great day!\n";
            break;
        }
        // if (userInput == "bye" || userInput == "Goodbye" || userInput == "see you") {
        //     cout << "Chatbot: Goodbye! Have a great day!\n";
        //     break;
        // }

        string response = getResponse(userInput);
        cout << "Chatbot: " << response << endl;
    }

    return 0;
}
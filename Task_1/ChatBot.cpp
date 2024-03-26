#include <iostream>
#include <string>
#include <algorithm>
#include <regex>
using namespace std;

regex byeRegex("bye|goodbye|go away|good bye|see you", regex_constants::icase);
// Function to get response based on user input
string getResponse(const string &userInput)
{
    // Predefined patterns and responses
    regex hiRegex("hi|hello|hey|yup|listen|start|let's start|let start", regex_constants::icase);
    regex howAreYouRegex("how are you\\?|how do you do", regex_constants::icase);
    regex whoAreYouRegex("who are you?|who are you|introduce|introduce yourself|tell me about yourself|tell me yourself");

    // Pattern matching and response selection
    if (regex_search(userInput, hiRegex))
    {
        return "Hello! How can I assist you?";
    }
    else if (regex_search(userInput, howAreYouRegex))
    {
        return "I'm just a chatbot, but thanks for asking!";
    }
    else if (regex_search(userInput, whoAreYouRegex))
    {
        return "I'm your trusty chatbot, Think of me as your digital sidekick, ready to engage in conversation, and help you navigate the vast expanse of the internet. \nSo, what can I do for you today?";
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
        transform(userInput.begin(), userInput.end(), userInput.begin(), ::tolower); // Convert input to lowercase
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
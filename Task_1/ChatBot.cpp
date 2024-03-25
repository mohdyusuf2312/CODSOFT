#include<iostream>
#include<string>
#include<algorithm>
#include <regex>
using namespace std;

// Function to get response based on user input
string getResponse(const string& userInput) {
    // Predefined patterns and responses
    regex hiRegex("hi|hello|hey|yup|listen", regex_constants::icase);
    regex howAreYouRegex("how are you\\?|how do you do", regex_constants::icase);
    regex byeRegex("bye|goodbye|go away|good bye", regex_constants::icase);

    // Pattern matching and response selection
    if (regex_search(userInput, hiRegex)) {
        return "Hello! How can I assist you?";
    } else if (regex_search(userInput, howAreYouRegex)) {
        return "I'm just a chatbot, but thanks for asking!";
    } else if (regex_search(userInput, byeRegex)) {
        return "Goodbye! Have a great day!";
    } else {
        return "I'm sorry, I didn't understand that.";
    }
}

int main() {
    cout << "Welcome to the ChatBot!\n";
    cout << "You can start chatting. Or Type 'bye' to exit.\n";
    
    string userInput;
    while (true) {
        cout << "You: ";
        getline(cin, userInput);
        transform(userInput.begin(), userInput.end(), userInput.begin(), ::tolower); // Convert input to lowercase
        if (userInput == "bye" || userInput == "Goodbye" || userInput == "see you") {
            cout << "Chatbot: Goodbye! Have a great day!\n";
            break;
        }
        
        string response = getResponse(userInput);
        cout << "Chatbot: " << response << endl;
    }
    
    return 0;
}
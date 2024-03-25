#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string getResponse(const string& userInput) {
    // Pattern matching and response selection
    if (userInput == "hello" || userInput == "hey" || userInput == "hi" || userInput == "yup" || userInput == "listen") {
        return "Hello! How can I assist you?";
    } else if (userInput == "how are you\\?" || userInput == "how do you do\\?") {
        return "I'm just a chatbot, but thanks for asking!";
    } else if (userInput == "bye" || userInput == "go away" || userInput == "goodbye" || userInput == "good bye") {
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
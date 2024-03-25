#include <iostream>
#include <string>

using namespace std;

int main() {
    cout << "Welcome to the ChatBot!\n";
    cout << "You can start chatting. Or Type 'bye' to exit.\n";
    
    string userInput;
    while (true) {
        cout << "You: ";
        getline(cin, userInput);
        
        if (userInput == "bye" || userInput == "Goodbye" || userInput == "see you") {
            cout << "Chatbot: Goodbye! Have a great day!\n";
            break;
        }
        
        
    }
    
    return 0;
}
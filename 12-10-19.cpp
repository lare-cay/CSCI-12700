/*Name: Clare Lee
Email: Clare.Lee94@myhunter.cuny.edu
Date: December 10, 2019
This program asks for dollahs and then keeps asking for spend amounts until spent */

#include <iostream>
using namespace std;

int main(){
    float amount;
    cout << "Please enter the initial dollar amount: ";
    cin >> amount;

    while (amount > 0){
        float spend;
        cout << "Please enter the amount you spent: ";
        cin >> spend;
        amount = amount - spend;
        cout << "You now have $" << amount << " remaining" << "\n"; 
    }
    
    cout << "You now have $" << amount << " remaining" << endl; 
    cout << "Your initial amount has been entirely spent";
return 0;
}

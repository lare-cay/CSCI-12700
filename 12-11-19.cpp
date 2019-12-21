/*Name: Clare Lee
Email: Clare.Lee94@myhunter.cuny.edu
Date: December 11, 2019
This program asks for whole num and prints out two's complement */

#include <iostream>
using namespace std;

int main(){
    int n, x, b;
    cout << "Enter a number between -31 and 31: ";
    cin >> n;
    if (n < 0){
        cout << 1;
        x = (32 + n);
    }
    else {
        cout << 0;
        x = n;
    }
    b = 16;
    while (b > 0.5) {
        if (x >= b){
            cout << 1;
        }
        else {
            cout << 0;
        }
        x = x % b;
        b = (b/2);
    }
    cout << "\n";
return 0;
}

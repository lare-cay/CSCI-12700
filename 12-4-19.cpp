/*Name: Clare Lee
Email: Clare.Lee94@myhunter.cuny.edu
Date: December 4, 2019
This program converts f to c*/

#include <iostream>
using namespace std;

int main(){
    float deg;
    cout << "Enter degrees in Farenheit: ";
    cin >> deg;
    cout << fixed << (deg-32.0)* (5.0/9.0);
return 0;
}

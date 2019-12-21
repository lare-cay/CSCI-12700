/*Name: Clare Lee
Email: Clare.Lee94@myhunter.cuny.edu
Date: December 9, 2019
This program asks for weekly salary until a positive number is giver*/

#include <iostream>
using namespace std;

int main(){
    int salary;
    cout << "Please enter your salary: ";
    cin >> salary;

    while (salary < 0){
        cout << "Entered a negative number." << endl;
        cout << "Please enter your salary: "; 
        cin >> salary; 
    }
    cout << "Your weekly salary is $" << salary << endl;
    return 0;
}

    

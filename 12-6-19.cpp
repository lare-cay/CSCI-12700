/*Name: Clare Lee
Email: Clare.Lee94@myhunter.cuny.edu
Date: December 4, 2019
This program converts f to c*/

#include <iostream>
using namespace std;

int main(){
    int grade = 0;
    cout << "Enter average grade: ";
    cin >> grade;
    if (grade < 60){
        cout << "Your letter grade is F";
        }
    else if (grade >= 60 && grade < 80){
        cout << "Your letter grade is C or D";
        }
    else if (grade >= 80 && grade < 90){
        cout << "Your letter grade is B";
        }
    else
        cout << "Your letter grade is A"; 
return 0;
}

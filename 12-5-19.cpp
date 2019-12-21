/*Name: Clare Lee
Email: Clare.Lee94@myhunter.cuny.edu
Date: December 5, 2019
This program takes 2 num and draws a grid*/

#include <iostream>
using namespace std;

int main(){
    int row, col;
    cout << "Enter the number of rows: ";
    cin >> row;
    cout << "Enter the number of column: ";
    cin >> col;
    for (int x = 0; x < row; x++) {
        for (int y = 0; y < col; y++) {
            cout << ((x+y+1)%2);
            }
        cout << endl;
        }
return 0;
}

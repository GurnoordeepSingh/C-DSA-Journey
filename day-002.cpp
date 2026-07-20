#include<iostream> //for input output
#include<cmath> //for mathematical functions
using namespace std;
int main() {
    string sentence="Hello i came here.";
    cout<<sentence<<endl;
    cout<<"sentence length="<<sentence.length()<<endl;
    cout<<"first character="<<sentence[0]<<endl;
    sentence[13]='t'; //you use single quotes for single character change
    cout<<sentence<<endl;

    //find the position of a character in a string
    cout<<sentence.find("am")<<endl;
    //find some characters from starting point to end point
    cout<<sentence.substr(6,6)<<endl; //form index 6, 6 positions forward

    //NUMBERS
    cout<<10/3<<endl; //gives 3 because both are integers
    cout<<10.0/3.0<<endl; //gives 3.33333 because both are double, if any one is double then the result will also be double
    
    //MATH FUNCTIONS
    cout<<"power="<<pow(2,5)<<endl;
    cout<<"square root="<<sqrt(25.5)<<endl;
    cout<<"round="<<round(2.5)<<endl; //rounds to nearest integer
    cout<<"floor="<<floor(2.8)<<endl; // rounds to smaller integer
    cout<<"ceil="<<ceil(2.2)<<endl; // rounds to larger integer
    cout<<"max="<<max(2,5)<<endl; //fmax and max are same, fmax is for double and max is for int
    //opposite of max is min
    
    return 0; 
}
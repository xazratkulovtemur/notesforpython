#include<iostream>
using namespace std;
int main() {
  int random=345;
  int guess, counter=0;
   cout<<"Enter the number of guesses:";
   while(true){
     cin>>guess;
     if (guess < random) {
       cout<<"Too low";
       counter ++;
     }
     else if (guess>random){
       cout<<"Too high";
       counter ++;
     }
     else {
       cout<<"correct";
       break;
     }
     if (counter%5==0) {
       if(random%2==0) {
         cout<<"It is even";}}
     if (counter%5==0) {
       if(random%5==0) {
         cout<<"It is multiple of 5!";
       }
       else {
         cout<<"It is odd, and not multiple of 5!";
       }
      }


     }
return 0;
}


#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main(){
    float t,a,b,c,d;
    long long time = 0;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>a>>b>>c>>d;
        if (b>=a){
            cout<<b;
        }
        else if( c-d < 0){
            cout<<-1;
        }
        else{
            cout<< (b+ ( ceil((a-b)/(c-d)) *c ));
        }
    }
    return 0;
}

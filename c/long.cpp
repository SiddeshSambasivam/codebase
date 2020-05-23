#include<iostream>
#include<sstream>
using namespace std;

int main(){
    int t, len;
    len=0;
    char end;
    cin>>t;
    stringstream ss;
    while(t!=0){
        char word[100];
        cin>>word;
        for(int i=0; word[i]!='\0'; i++){
            len+=1;
            end = word[i];
        }
        ss<<len-2; string len_str;
        ss>>len_str;
        if (len > 10){
            string nametext= word[0]+len_str+word[len-1];
            cout<<nametext;
        }
        else{
            cout<<word;
        }
        t-=1;
    }
    return 0;
}

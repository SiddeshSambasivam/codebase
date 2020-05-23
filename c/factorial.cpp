#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int t,n,z,j;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n;
        z = 0;
        if(n<=4) cout<<0;
        else{
            j = 1;
            while(n/(5^j)<=0){
                z+= n/(5^j);
            }
            cout<<z;
        }
    }
    return 0;
}

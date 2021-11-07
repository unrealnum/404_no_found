#include<bits/stdc++.h>
using namespace std;
int  main(void){
    int v,s,hour,min;
    cin>>s>>v;
    int sum=(int)(s/v)+10;
    if(s%v!=0){          //这一步比后面-1更全面
        sum++;
    }
    int result;
    if(sum>480){
        result=32*60-sum;
        hour=result/60;
        min=result%60;
        if(hour<10){
            cout<<"0"<<hour<<":";
        }
        else{
            cout<<hour<<":";
        }
        if(min<10){
            cout<<"0"<<min;
        }
        else{
            cout<<min;
        }
    }
    else{
        result=8*60-sum;
        hour=result/60;
        min=result%60;
        if(hour<10){
            cout<<"0"<<hour<<":";
        }
        else{
            cout<<hour<<":";
        }
        if(min<10){
            cout<<"0"<<min;
        }
        else{
            cout<<min;
        }
    }
}
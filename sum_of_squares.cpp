#include<iostream>
using namespace std;
 
int main()
{
	int n,i,sum=0,d;                
	cout<<"Enter any number:";        #inputing number n
	cin>>n;                           
 
	for(i=1;i<=n;i++)
	{
		d=i*i;                       #find square of i
		sum=sum+d;                   #add to previous sm
	}
 
	cout<<"Sum="<<sum;            #output sum of squaresof all natural no.s from 1 to n
	return 0;
}

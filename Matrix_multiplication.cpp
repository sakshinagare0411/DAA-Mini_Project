#include <iostream>

using namespace std;

int main()
{
  int a[50][50],b[50][50],c[50][50],i,j,n,m,p,q,sum;
  cout<<"matric a is ::\n";
  cout<<"enter row and column no:\n";
  cin>>m>>n;
  cout<<"element of a::\n";
  for(i=0;i<m;i++)
  {
      for(j=0;j<n;j++)
      {
          cin>>a[i][j];
      }
  }
  cout<<"matrix a is::\n";
  for(i=0;i<m;i++)
  {
      for(j=0;j<n;j++)
      {
          cout<<a[i][j]<<"  ";
      }
      cout<<"\n";
  }
   cout<<"matric b is ::\n";
  cout<<"enter row and column no:\n";
  cin>>q>>p;
  cout<<"element of b::\n";
  for(i=0;i<q;i++)
  {
      for(j=0;j<p;j++)
      {
          cin>>b[i][j];
      }
  }
  cout<<"matrix b is::\n";
  for(i=0;i<q;i++)
  {
      for(j=0;j<p;j++)
      {
          cout<<b[i][j]<<"  ";
      }
      cout<<"\n";
  }
 
  if(n==q)
  {
      cout<<"multiplication is::\n";
     
      for(i=0;i<m;i++)
      {
          for(j=0;j<p;j++)
          {
              c[i][j]=0;
              for(int k=0;k<n;k++)
              {
                c[i][j]+= a[i][k]*b[k][j];
              }
          }
      }
     
     for(i=0;i<m;i++)
      {
          for(j=0;j<p;j++)
          {
              cout<<c[i][j]<<" ";
          }
          cout<<"\n";
      }
     
  }
  else
  {
      cout<<"matrix multiplication not possible";
  }
 
    return 0;
}

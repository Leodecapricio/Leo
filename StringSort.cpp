#include<iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter the number of strings: " << endl;
    cin >> n;
    string* arr;
    int* index;
    arr = new string[n];
    index = new int[n];
    int i;
    for(i=0; i<n; i++)
    {
        index[i]=i;
    }
    cout << "Enter strings:\n";
    for(i=0; i<n; i++)
    {
        cin >> arr[i];
    }
    int j;
    for(i=0; i<n-1; i++)
    {
        int min=i;
        for(j=i+1; j<n; j++)
        {
            if(arr[index[min]].compare(arr[index[j]])>0)
                min=j;
        }
        int temp;
        temp=index[i];
        index[i]=index[min];
        index[min]=temp;
    }
    count << "Strings in sorted order are:\n" << endl;
    for(i=0; i<n; i++)
        cout << arr[index[i]] << endl;
  return 0;
}

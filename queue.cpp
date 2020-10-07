#include<iostream>

using namespace std;

class queue
{
    int* arr;
    int front;
    int rear;
    int size;

public:

    queue(int a)
    {
        size=a;
        arr = new int[size];
        rear=-1;
        front=-1;
    }

    void insert(int data)
    {
        if(rear==size-1)
        {
            cout << "Insertion not possible! Queue is full! " << endl;
        }
        else
        {
            rear++;
            arr[rear]=data;
            if(rear==0)
                front++;
        }
    }

    int remove()
    {
        if(front==-1 && rear==-1)
            cout << "Deletion not possible! Queue is empty!" << endl;
        else
        {
            int x=arr[front];
            front++;
            if(front>rear)
            {
                front=-1;
                rear=-1;
            }
            return x;
        }
    }

    void display()
    {
        int i;
        if(front==-1 && rear==-1)
            cout << "No elements to display!" << endl;
        else
        {
            for(i=front; i<=rear; i++)
            cout << arr[i] << endl;
        }
    }

    void clear()
    {
        front=-1;
        rear=-1;
    }

    /*void ReverseList(queue x)
    {
        if(x.rear==-1)
            return;
        queue temp(size);
        while(x.rear!=x.front)
        {
            temp.insert(x.remove());
        }
        insert(x.remove());
        ReverseList(temp);
    }*/
    void ReverseList(queue x)
    {
	    int temp;
	    if(x.rear==-1)
	    {
		    return;
	    }
	    else
	    {
		     temp = x.remove();
	    }
	    ReverseList(x);
	    x.insert(temp);
    }

    void ReverseSublist(int a,int b)
    {
        queue temp(size);
        while(front!=a)
        {
            temp.insert(remove());
        }
        queue temp1(size);
        while(front!=b+1)
        {
            temp1.insert(remove());
        }
        queue temp2(size);
        temp2.ReverseList(temp1);
        queue temp3(size);
        while(rear!=-1)
        {
            temp3.insert(remove());
        }
        while(temp.rear!=-1)
            insert(temp.remove());
        while(temp2.rear!=-1)
            insert(temp2.remove());
        while(temp3.rear!=-1)
            insert(temp3.remove());
    }

    void SortQueue()
    {
        int i;
        for(i=rear; i>0; i--)
        {
            queue x(size);
            int max=-9999999,index;
            int flag;
            if(i==rear)
                flag=-1;
            else
                flag=i+1;
            while(front!=flag)
            {
                int t = remove();
                if(t>max)
                {
                    max=t;
                    index=front-1;
                }
                x.insert(t);
            }
            queue y(size);
            while(rear!=-1)
            {
                y.insert(remove());
            }
            while(x.rear!=-1)
            {
                int flag=0;
                if(x.front==index)
                    flag=1;
                if(flag==1)
                {
                    x.remove();
                }
                else
                {
                    flag=0;
                    insert(x.remove());
                }

            }
            insert(max);
            while(y.rear!=-1)
            {
                insert(y.remove());
            }

        }
    }

};

int main()
{
    int s;
    cout << "Enter maximum size of the queue: " << endl;
    cin >> s;
    queue A(s);
    cout << endl;
    cout << "1. Enqueue an element" << endl;
    cout << "2. Dequeue an element" << endl;
    cout << "3. Display the queue" << endl;
    cout << "4. Clear" << endl;
    cout << "5. Reverse the queue" << endl;
    cout << "6. Reverse the sublist" << endl;
    cout << "7. Sort the queue" << endl;
    cout << endl;
    int choice,flag=0;
    while(flag==0)
    {
        cout << "Enter your choice: ";
        cin >> choice;
        switch(choice)
        {
            case 1: {
                         int a;
                         cout << "Enter the data you want to enqueue: " << endl;
                         cin >> a;
                         A.insert(a);
                         cout << "Queue after enqueue is:\n";
                         A.display();
                         break;
                    }

            case 2: {
                         cout << "Dequeued element is " << A.remove() << endl;
                         cout << "Queue after dequeue is:\n";
                         A.display();
                         break;
                    }

            case 3: {
                         cout << "Queue is:\n";
                         A.display();
                         break;
                    }

            case 4: {
                         A.clear();
                         break;
                    }

            case 5: {
                         queue B(s);
                         B=A;
                         A.clear();
                         A.ReverseList(B);
                         cout << "Queue after reversing is: " << endl;
                         A.display();
                         break;
                    }

            case 6: {
                         int a,b;
                         cout << "Enter the two indexes: " << endl;
                         cin >> a >> b;
                         A.ReverseSublist(a,b);
                         cout << "Queue after reversing is: " << endl;
                         A.display();
                         break;
                    }

            case 7: {
                         A.SortQueue();
                         cout << "Queue after sorting is: " << endl;
                         A.display();
                         break;
                    }

           default: {
                         flag=1;
                         break;
                     }

        }
    }
   return 0;
}



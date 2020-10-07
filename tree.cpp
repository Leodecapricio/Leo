#include<iostream>
using namespace std;

template<typename E>
struct Tnode
{
    E data;
    Tnode *left;
    Tnode *right;
};
Tnode<int> *root=NULL;
template<typename E>
struct node2
{
    E data;
    node2<E>* next;
    node2<E>* pre;
};
template<typename E>
Tnode<E>* new_node(E value)
{
    Tnode<E> *temp=new Tnode<E>;
    temp->data=value;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}
template<typename E>
node2<E>* getNode2(E key)
{
    node2<E>* temp=new node2<E>;
    temp->data=key;
    temp->next=NULL;
    temp->pre=NULL;
    return temp;
}

template <typename E>
class doubly_linkedList
{
  node2<E>* head;
  node2<E>* lastNode;
  int size;
  public:
      doubly_linkedList()
      {
          head=NULL;
          lastNode=NULL;
          size=0;
      }

      void append(E key)
      {
          if(head==NULL)
          { size++;
            head=getNode2(key);
            lastNode=head;
          }else{
          node2<E>* temp=lastNode;
          lastNode->next=getNode2(key);
          size++;
          lastNode=temp->next;
          lastNode->pre=temp;
          }
      }
       E getValue(node2<E>* temp)
      {
          return temp->data;
      }
      node2<E>* getFirstele()
      {
          return head;
      }
      void setFirstele(node2<E>* temp)
      {
          head=temp;
      }

      void print_2()
    {
        node2<E>* temp=head;
        while(temp!=NULL)
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
    }
    int total_ele()
    {return size;}

};
template <typename E>
void inorder(Tnode<E>* root)
{
  if(root!=NULL)
  {
    inorder(root->left);
    cout<<root->data<<"  ";
    inorder(root->right);
  }
}
template <typename E>
void convert_doubly(Tnode<E>* root,doubly_linkedList<E>& A)
{
  if(root!=NULL)
  {
    convert_doubly(root->left,A);
    A.append(root->data);
    convert_doubly(root->right,A);
  }
}
template <typename E>
void leaf_convert(Tnode<E>* root,doubly_linkedList<E>& B)
{
    if(root==NULL)
        return;
    if(root->left==NULL && root->right==NULL)
    {
        B.append(root->data);
        return;
    }
    if(root->left!=NULL)
      leaf_convert(root->left,B);
    if(root->right!=NULL)
      leaf_convert(root->right,B);
}
int cousin(Tnode<int>* root,int x,int y)
{
    Tnode<int>* temp=root;
    Tnode<int>* temp1;
    Tnode<int>* temp2;
    Tnode<int>* pre=NULL;
    int count1=0,count2=0;
    if(temp==NULL)
        return 0;
    if(temp->data==x)
        return 0;
    while(temp!=NULL)
    {
        if(temp->data >x)
        {
            pre=temp;
            temp=temp->left;
            count1++;
        }
        else if(temp->data < x)
        {
            pre=temp;
            temp=temp->right;
            count1++;
        }
        else {
                if(temp==NULL)
                return 0;
            temp1=pre;
            break;
        }
    }
    temp=root;
    pre=NULL;
    if(temp==NULL)
        return 0;
    if(temp->data==y)
        return 0;
    while(temp!=NULL)
    {
        if(temp->data >y)
        {
            pre=temp;
            temp=temp->left;
            count2++;
        }
        else if(temp->data < y)
        {
            pre=temp;
            temp=temp->right;
            count2++;
        }
        else {
                if(temp==NULL)
                return 0;
            temp2=pre;
            break;
        }
    }
    if(temp1!=temp2 && count1==count2)
        return 1;
    else return 0;
}
int main()
{
    root=new_node(67);
    root->left=new_node(34);
    root->right=new_node(98);
    root->left->left=new_node(3);
    root->left->right=new_node(38);
    root->right->left=new_node(87);
    root->right->right=new_node(102);
    root->left->left->left=new_node(1);
    inorder(root);
    int t=cousin(root,0,999);
    cout<<"\nt: "<<t<<endl;
    doubly_linkedList<int> A;
    doubly_linkedList<int> B;
   // convert_doubly(root,A);
    leaf_convert(root, B);
    B.print_2();
}

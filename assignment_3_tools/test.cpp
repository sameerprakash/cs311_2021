#include <stack>
#include <fstream>
#include <iostream>

using namespace std; 


int main (int count, char* previous_move[])
{
	stack<string> moves;
	
	ifstream fin("mymoves.dat",ios::in | ios::out);
  	
  	ofstream fout("mymoves.dat",ios::app);
  	
  	
  	
	
	if(string(previous_move[2]) == "zero")
	{
		cout<<"silent"; 
		
	}else{
		cout<<previous_move[2];
		fout<<previous_move[2];
		string m;
                while (getline(fin, m)) {
                   moves.push(m);
                   }
                   
        cout<<moves.top();
	
	}

	return 0;

}

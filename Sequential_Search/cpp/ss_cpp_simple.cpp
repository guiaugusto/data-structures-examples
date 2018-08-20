#include <iostream>
#include <vector>

using namespace std;

int main(){

  int number;
  vector<int> elements = {0, 1, 3, 4, 6, 19, 12};

  cout << "Say a number to find in the array container." << endl;
  cin >> number;

  for(int i = 0; i < elements.size(); i++){
    if(number == elements[i]){
      cout << "The number " << number << " exists in the array." << endl;
      return 0;
    }
  }

  cout << "The number is not in the array container." << endl;

  return 0;
}

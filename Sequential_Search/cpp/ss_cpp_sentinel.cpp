#include <iostream>
#include <vector>

using namespace std;

int main(){

  int number;
  vector<int> elements = {0, 1, 3, 4, 6, 19, 12};

  cout << "Say a number to find in the array container." << endl;
  cin >> number;

  elements.push_back(number);

  int i;

  for(i = 0; number < elements[i]; i++);

  if(i == elements.size()) {
    cout << "The number is not in the array container." << endl;
  } else {
    cout << "The number " << number << " exists in the array." << endl;
  }

  return 0;
}

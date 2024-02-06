#include <iostream>
#include <string>

using namespace std;

string cesar(string line, int key) {
  string alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  string crypt{""};
  for (int i = 0; i < line.size(); i++) {
    char c = line[i];
    crypt += alph[(alph.find(c) + key) % 26];
  }
  return crypt;
}

int main() {
  string line{"TEST"};
  cout << cesar(line, 3);
  return 0;
}
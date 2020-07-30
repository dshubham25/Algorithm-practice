/* You have 1000 bottles of wine, and exactly one bottle is poisoned. You need
to find the poisoned wine before your party starts in an hour. You have 10 rats
to test on to the find out which bottle is deadly. The poison takes effect after
an hour of consumption, so you only have one chance to run your rat poison
experiment , meaning you can't feed some rats wine and wait for an hour before
feeding them more wine. Assume each rat can drink as much wine as you feed it.
How do you find the poisoned wine? */

#include <bits/stdc++.h>
#include <cmath>
using namespace std;

int minRats(int n) {
  return ceil(log2());
}

int main(){
  int n = 1000;
  cout << "Minimum " << minRats(n)
       << " rat(s) are required" << endl;
  return 0;
}

#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
class ABBA {
 public:
    string canObtain(string initial, string target) {
        bool lastLetterWasB;
		while(target.size() >= initial.size()) {
            if(target == initial) {
            	return "Possible";    
           	 }
            if(target.substr(target.size() - 1) == "B") {
                lastLetterWasB = true;
                }
            else {
                lastLetterWasB = false;
                }
            target = target.substr(0, target.size()-1);
			if(lastLetterWasB) {
                reverse(target.begin(), target.end());
            }
            
            }
    	return "Impossible";
    }
    
  
};

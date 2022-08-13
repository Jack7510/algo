#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    if( argc > 1 )
    {
        vector<int> a = {};
        auto print = [](const int& n) {cout << ' ' << n ;};

        for(int i = 1; i < argc; i++ )
        {
            a.push_back(atoi(argv[i]));
        }

        for_each(a.begin(), a.end(), print);
        cout << "\n";
    }
}
#include <iostream>
using namespace std;

int main()
{
    int r1, c1, r2, i, j, k;
    int c2 = 1;

    cin >> r1 >> c1;
    cin >> r2;
    
    int a[r1][c1], b[r2][c2], res[r1][c2];

    cout << endl << "Input matrix:" << endl;
    for(i = 0; i < r1; ++i)
        for(j = 0; j < c1; ++j)
        {
            cin >> a[i][j];
        }

    cout << endl << "Input vector:" << endl;
    for(i = 0; i < r2; ++i)
        for(j = 0; j < c2; ++j)
        {
            cin >> b[i][j];
        }

    for(i = 0; i < r1; ++i)
        for(j = 0; j < c2; ++j)
        {
            res[i][j]=0;
        }
    
    for(i = 0; i < r1; ++i)
        for(j = 0; j < c2; ++j)
            for(k = 0; k < c1; ++k)
            {
                res[i][j] += a[i][k] * b[k][j];
            }

    cout << endl << "Result vector:" << endl;
    for(i = 0; i < r1; ++i)
    for(j = 0; j < c2; ++j)
    {
        cout << " " << res[i][j];
        if(j == c2-1)
            cout << endl;
    }

    return 0;
}

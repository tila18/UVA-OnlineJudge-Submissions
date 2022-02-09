#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <iterator>

// for part 1
std::map<std::string, int> characters_pt1 = { {"M" , 1000}, {"D" , 500}, {"C" , 100}, {"L" , 50}, { "X" , 10}, {"V" , 5}, {"I" , 1 } };

// for part 2
std::string arg1, arg2, arg3;
int solutions_found;

std::map<char, int> characters_pt2;
std::vector<int> possible_values { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; 

int roman_to_integer(std::string roman_number)
{
    int number = 0;
    for (int i = 0; i < roman_number.length(); i++) {
        std::string s;
        s.push_back(roman_number[i]);

        int firstNumber = characters_pt1[s];

        if (i == roman_number.length() - 1) {
            number += firstNumber;
        }
        else 
        {
            std::string s2;
            s2.push_back(roman_number[i+1]); 
            int secondNumber = characters_pt1[s2];

            if (firstNumber < secondNumber) {
                number -= firstNumber;
            }
            else {
                number += firstNumber;
            }
        }
    }

    return number;
}

// used to create integers from strings like '001' returning NULL as it's a faulty number or '1203' returning 1203
int chars_to_int(std::string chars, std::map<char, int> characters_pt2)
{
    std::string num_string;
    for (char& c : chars) 
    {
        num_string += std::to_string(characters_pt2[c]);
    }
    if (num_string.length() > 1 && num_string[0] == '0')
    {
        return NULL;
    } 
    return std::stoi(num_string);
}

void dfs(int depth, int s, int i, std::vector<int>& cmb, const std::vector<int>& v, std::string case_chars)
{
    if (depth == s)
    {
        do
        {
            if (solutions_found > 2) 
            {
                break;
            }

            //assign a letter to a number in current combo
            int counter = 0;
            for (char c: case_chars)
            {
                if (counter < case_chars.length())
                {
                    characters_pt2[c] = cmb[counter];
                    counter++;
                }
            }
            
            int a = chars_to_int(arg1, characters_pt2);
            int b = chars_to_int(arg2, characters_pt2);
            int c = chars_to_int(arg3, characters_pt2);
            
            if ((a && b && c) && (a * b * c > 0))
            {
                if (a + b == c)
                {
                    solutions_found++;
                }
            }
        } while (std::next_permutation(cmb.begin(), cmb.end())); // 
    }
    else
    {
        for (int j = i + 1; j < (int)v.size(); ++j)
        {
            cmb.push_back(v[j]);
            dfs(depth + 1, s, j, cmb, v, case_chars);
            cmb.pop_back();
        }
    }
}


std::string removeSpaces(std::string str)
{
    str.erase(remove(str.begin(), str.end(), ' '), str.end());
    str.erase(remove(str.begin(), str.end(), '\n'), str.end());
    return str;
}

int main()
{
    // prepare table
    characters_pt2['I'] = 0;
    characters_pt2['X'] = 0;
    characters_pt2['C'] = 0;
    characters_pt2['M'] = 0;
    characters_pt2['V'] = 0;
    characters_pt2['L'] = 0;
    characters_pt2['D'] = 0;

    std::sort(possible_values.begin(), possible_values.end());

    std::string temp;

    while (true)
    {
        std::getline(std::cin, temp);

        if (temp == "#")
            break;

        std::string input = removeSpaces(temp);

        solutions_found = 0;
        std::string output;

        int pos1 = input.find('+');
        int pos2 = input.find('=');

        arg1 = input.substr(0, pos1);
        arg2 = input.substr(pos1 + 1, pos2 - pos1 - 1);
        arg3 = input.substr(pos2 + 1, input.length());


        // check what characters need to be tested
        std::string full_string = arg1 + arg2 + arg3;
        std::string case_chars;
        for (char& c : full_string)
        {
            if (case_chars.find(c) == std::string::npos)
                case_chars += c;
        }
        int length = case_chars.length();

        std::vector<int> combos;
        std::string arguments[] = { arg1, arg2, arg3 };

        //Invalid input // any argument has more than 9 letters 
        if ((arg1.length() > 9 || arg2.length() > 9 || arg3.length() > 9))
        {
            output = "Invalid input";
        }
        else
        {
            //PART 1
            int int1 = roman_to_integer(arg1);
            int int2 = roman_to_integer(arg2);
            int int3 = roman_to_integer(arg3);

            if ( int1 * int2 * int3 != 0 && int1 + int2 == int3)
            {
                output += "Correct";
            }
            else
            {
                output += "Incorrect";
            }
            
            // PART 2
            if (length > 1)
            {
                //recursively called
                dfs(0, length, -1, combos, possible_values, case_chars);
            }

            if (solutions_found == 0)
            {
                output += " impossible";
            }
            else if (solutions_found == 1)
            {
                output += " valid";
            }
            else
            {
                output += " ambiguous";
            }
        }

        if (!output.empty())
        {
            std::cout << output << std::endl;
        }
    }
    return 0;
}


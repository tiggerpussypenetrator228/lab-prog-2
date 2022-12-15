#include <iostream>

#include <stack>

#include <string>

struct verification_info_t
{
  bool verified;

  int position;
  char expected;
  char found;
};

verification_info_t verify_parenthesis(const std::string& text)
{
  verification_info_t info;
  info.verified = true;

  std::stack<char> expect = {};
  int position = 0;
  for (char curchar : text)
  {
    switch (curchar)
    {
      case('('):
      {
        expect.push(')');

        break;
      }
      case('{'):
      {
        expect.push('}');

        break;
      }
      case('['):
      {
        expect.push(']');

        break;
      }
      case(')'):
      case(']'):
      case('}'):
      {
        if (expect.size() <= 0)
        {
          info.verified = false;

          info.position = position;
          info.found = curchar;
          info.expected = curchar == ')' ? '(' : curchar == ']' ? '[' : '{';

          return info;
        }

        char expected = expect.top();

        if (curchar != expected)
        {
          info.verified = false;

          info.position = position;
          info.found = curchar;
          info.expected = expected;

          return info;
        }
        
        expect.pop();

        break;
      }
    }

    position++;
  }

  if (expect.size() > 0)
  {
    info.verified = false;

    info.position = text.length();
    info.expected = expect.top();
    info.found = ' ';
  }
  
  return info;
}

int main(int argc, char** argv)
{
  std::string input;
  std::cin >> input;

  verification_info_t info = verify_parenthesis(input);

  if (info.verified)
  {
    std::cout << "Parenthesis verified successfully." << std::endl;
  }
  else
  {
    std::cout << "Verification failed:" << std::endl;
    std::cout << "Position: " << info.position << std::endl;
    std::cout << "Expected: " << info.expected << " Found : " << info.found << std::endl;
  }

  return 0;
}

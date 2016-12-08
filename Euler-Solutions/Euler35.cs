using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication3
{
    class Program
    {
        static void Main(string[] args)
        {
            int totalNumberOfPrimes = 0;
            string numberAsString = "";
            int tempInt = 0;
            bool isPrimeFlag;

            for (int number = 2; number < 1000000; number++)
            {
                if (isPrime(number) == false)
                {
                    continue;
                }

                numberAsString = number.ToString();
                isPrimeFlag = true;

                for (int i = 1; i < numberAsString.Length; i++)
                {
                    numberAsString = rotateNumber(numberAsString);

                    if (isPrime(int.Parse(numberAsString)) == false)
                    {
                        isPrimeFlag = false;
                        break;
                    }
                }

                if (isPrimeFlag)
                {
                    Console.WriteLine(number.ToString());
                    totalNumberOfPrimes++;
                }
            }
            Console.ReadLine();
        }

        static string rotateNumber(string number)
        {
            string numberAsString = number.ToString();
            numberAsString = numberAsString.Substring(1) + numberAsString.Substring(0, 1);

            return numberAsString;

        }
        static bool isPrime(int number)
        {
            if (number < 2)
            {
                return false;
            }
            if (number == 2)
            {
                return true;
            }

            for (int i = 2; i < (number/2) + 1; i++)
            {
                if (number%i == 0)
                {
                    return false;
                }
            }

            return true;
        }
    }
}

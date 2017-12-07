using System;
using System.Collections.Generic;
using System.IO;

namespace Day5
{
    public static class Program
    {
        private static List<int> input = new List<int>() { 0, 3, 0, 1, -3 };
        private static int AmountOfStepsMade = 0;

        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                InitializeInput();
            }

            var index = 0;
            while(index < input.Count)
            {
                var currentIndex = index;

                // Obtain the new index value
                index = input[currentIndex] + currentIndex;

                // Increase the current index value
                if((index - currentIndex) >= 3)
                {
                    input[currentIndex]--;
                }
                else
                {
                    input[currentIndex]++;
                }
                

                AmountOfStepsMade++;
            }
            Console.WriteLine($"Amount of steps required to get out of the index: {AmountOfStepsMade}");
        }

        private static void InitializeInput()
        {
            input = new List<int>();
            foreach(var line in File.ReadAllLines("input.txt"))
            {
                input.Add(int.Parse(line));
            }
        }
    }
}

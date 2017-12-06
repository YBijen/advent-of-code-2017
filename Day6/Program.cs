using System;
using System.Collections.Generic;
using System.Linq;

namespace Day6
{
    class Program
    {
        private static string ASSIGNMENT_INPUT = "4 10 4 1 8 4 9 14 5 1 14 15 0 15 3 5";
        private static List<string> MemoryBankStates = new List<string>();
        private static int AmountOfRedistributions = 0;

        static void Main(string[] args)
        {
            var memoryBanks = (args == null || args.Length == 0) ? FillMemorybanks(ASSIGNMENT_INPUT) : FillMemorybanks(args[0]);
            var memoryBanksLength = memoryBanks.Count;
            var currentState = MemoryBankToString(memoryBanks);

            while (!MemoryBankStates.Contains(currentState))
            {
                // Add value to MemoryBank states
                MemoryBankStates.Add(currentState);

                Console.WriteLine(currentState);

                // Find index highest memory bank
                var startingIndex = memoryBanks.IndexOf(memoryBanks.Max());

                // Obtain value index highest memory bank
                var value = memoryBanks.Max();

                // Set the value of the highest memory bank to 0
                memoryBanks[startingIndex] = 0;

                // Loop through list and fill memory banks
                for(var i=1; i<=value; i++)
                {
                    // Calculate index
                    var index = (startingIndex + i < memoryBanksLength)
                        ? startingIndex + i
                        : (startingIndex + i) % memoryBanksLength;

                    memoryBanks[index]++;
                }

                currentState = MemoryBankToString(memoryBanks);

                AmountOfRedistributions++;
            }

            Console.WriteLine($"Restributions before infinite loop cycle: {AmountOfRedistributions}. This happened after {CalculateCycleDifference(currentState)} cycles.");
        }

        private static string MemoryBankToString(List<int> list) => string.Join("|", list);

        private static int CalculateCycleDifference(string sequence)
        {
            return (MemoryBankStates.Count) - MemoryBankStates.IndexOf(sequence);
        }

        private static List<int> FillMemorybanks(string input)
        {
            return input.Split(' ').Select(v => int.Parse(v)).ToList();
        }
    }
}
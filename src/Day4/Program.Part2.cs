using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day4
{
    public static class Program
    {
        private static string StringToUse;

        public static void Main(string[] args)
        {
            if (args.Length > 0 && !string.IsNullOrEmpty(args[0])) StringToUse = args[0];
            Console.WriteLine($"Amount of valid PassPhrases in the file are: {AmountOfValidPassPhrasesInFile()}");
        }

        private static int AmountOfValidPassPhrasesInFile()
        {
            int validLines = 0;

            if(!string.IsNullOrEmpty(StringToUse))
            {
                validLines = ValidPassphrase(StringToUse) ? 1 : 0;
            }
            else
            {
                foreach (var line in File.ReadAllLines("input.txt"))
                {
                    if(ValidPassphrase(line))
                    {
                        validLines++;
                    }
                }
            }

            return validLines;
        }

        private static bool ValidPassphrase(string phrase)
        {
            var words = OrderEachWordAlphabetically(phrase.Split(" "));
            for (var i = 0; i < words.Length; i++)
            {
                for (var j = i+1; j < words.Length; j++)
                {
                    if (words[i] == words[j])
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        private static string[] OrderEachWordAlphabetically(string[] words)
        {
            var orderedWords = new List<string>();
            foreach(var word in words)
            {
                orderedWords.Add(string.Join("", word.OrderBy(c => c)));
            }
            return orderedWords.ToArray();
        }
    }
}

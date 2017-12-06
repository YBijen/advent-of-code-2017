using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day2
{
    class Program
    {
        static List<List<int>> input = new List<List<int>>();
        static List<int> resultList = new List<int>();

        static void Main(string[] args)
        {
            ProcessInput();

            //FillListPart1();
            FillListPart2();

            Console.WriteLine($"Result is: {resultList.Sum()}");
        }

        static void FillListPart1()
        {
            foreach (var list in input)
            {
                resultList.Add((list.Max() - list.Min()));
            }
        }

        static void FillListPart2()
        {
            foreach (var list in input)
            {
                ProcessListOfPart2(list.OrderByDescending(v => v).Distinct().ToList());
            }
        }

        static void ProcessListOfPart2(List<int> list)
        {
            for (var i = 0; i < list.Count; i++)
            {
                for (var j = i + 1; j < list.Count; j++)
                {
                    if (list[i] % list[j] == 0)
                    {
                        resultList.Add(list[i] / list[j]);
                        return;
                    }
                    //else if (list[j] % list[i] == 0)
                    //{
                    //    resultList.Add(list[j] / list[i]);
                    //    return;
                    //}
                }
            }
        }

        static void ProcessInput()
        {
            foreach(var line in File.ReadAllLines("input.txt"))
            {
                input.Add(line.Split('\t').Select(v => int.Parse(v)).ToList());
            }
        }
    }
}
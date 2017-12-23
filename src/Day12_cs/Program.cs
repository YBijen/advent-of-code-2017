using System;
using System.Collections.Generic;
using System.Linq;

namespace Day12_cs
{
    class Program
    {
        private static List<string> inp = new List<string> { "0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4", "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5" };
        private static List<InputItem> input = new List<InputItem>();
        private static List<InputItem> values = new List<InputItem>();

        private static List<InputItem> reducedInput = new List<InputItem>();
        private static List<List<InputItem>> Groups = new List<List<InputItem>>();

        private static List<InputItem> ToDelete = new List<InputItem>();

        private static int CompareValue = 0;

        static void Main(string[] args)
        {
            inp = System.IO.File.ReadAllLines("input.txt").ToList();

            input = inp.Select(line => new InputItem
            {
                Index = int.Parse(line.Split("<->")[0].Trim()),
                Associated = line.Split("<->")[1].Trim().Split(",").Select(v => int.Parse(v.Trim())).ToList()
            }).ToList();

            // Very inefficient way of duplicating the input list
            foreach(var i in input)
            {
                reducedInput.Add(i);
            }


            while(reducedInput.Count > 0)
            {
                values = new List<InputItem>();

                foreach(var td in ToDelete)
                {
                    reducedInput.Remove(td);
                }
                ToDelete = new List<InputItem>();

                if(reducedInput.Count <= 0)
                {
                    break;
                }

                CompareValue = reducedInput[0].Index;

                foreach (var inp in reducedInput)
                {
                    //Console.WriteLine("Current index: " + inp.Index);

                    if (values.Contains(inp))
                    {
                        continue;
                    }

                    if (inp.Index == CompareValue)
                    {
                        values.Add(inp);
                        ToDelete.Add(inp);
                        foreach (var c in inp.Associated)
                        {
                            Modify(input.First(v => v.Index == c));
                        }
                    }
                    else if (inp.Associated.Contains(CompareValue))
                    {
                        Modify(inp);
                    }
                    else if (inp.Associated.Any(c => IsConnectedTo0(c, inp.Index)))
                    {
                        Modify(inp);
                    }
                }

                Groups.Add(values);
            }

            Console.WriteLine($"Final Result is that we have the following amount of groups: {Groups.Count}");
            Console.WriteLine($"Input: {string.Join(" | ", input.Select(i => i.Index))}");
            Console.WriteLine($"Groups: {string.Join(" | ", Groups.SelectMany(g => g.Select(o => o.Index)).OrderBy(i => i))}");
            Console.WriteLine($"Does the output match the input --> {(input.Select(i => i.Index).OrderBy(i => i).SequenceEqual(Groups.SelectMany(g => g.Select(o => o.Index)).OrderBy(i => i)) ? "YES" : "NO")}");
            Console.Read();
        }

        static void Modify(InputItem ii)
        {
            if(!values.Contains(ii))
            {
                values.Add(ii);
            }
            ToDelete.Add(ii);
        }

        static bool IsConnectedTo0(int i, int prevI)
        {
            var elem = input.First(inp => inp.Index == i);

            if (elem.Associated.Contains(CompareValue))
            {
                return true;
            }
            else
            {
                return elem.Associated.Where(a => a != prevI).Any(c => values.Any(v => v.Index == c) || IsConnectedTo0(c, elem.Index));
            }
        }
    }

    public class InputItem
    {
        public int Index { get; set; }
        public List<int> Associated { get; set; }
    }
}
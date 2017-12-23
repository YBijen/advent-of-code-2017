//using System;
//using System.Collections.Generic;
//using System.Linq;

//namespace Day12_cs
//{
//    class Program
//    {
//        private static List<string> inp = new List<string> { "0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4", "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5" };
//        private static List<InputItem> input = new List<InputItem>();
//        private static List<InputItem> values = new List<InputItem>();

//        private static int CompareValue = 0;

//        static void Main(string[] args)
//        {
//            inp = System.IO.File.ReadAllLines("input.txt").ToList();

//            input = inp.Select(line => new InputItem
//            {
//                Index = int.Parse(line.Split("<->")[0].Trim()),
//                Associated = line.Split("<->")[1].Trim().Split(",").Select(v => int.Parse(v.Trim())).ToList()
//            }).ToList();

//            CompareValue = input[0].Index;

//            foreach (var inp in input)
//            {
//                Console.WriteLine("Current index: " + inp.Index);

//                if(values.Contains(inp))
//                {
//                    continue;
//                }

//                if(inp.Index == CompareValue)
//                {
//                    values.Add(inp);
//                    foreach(var c in inp.Associated)
//                    {
//                        values.Add(input.First(v => v.Index == c));
//                    }
//                }
//                else if(inp.Associated.Contains(CompareValue))
//                {
//                    values.Add(inp);
//                }
//                else if(inp.Associated.Any(c => IsConnectedTo0(c, inp.Index)))
//                {
//                    values.Add(inp);
//                }
//            }
            
//            Console.WriteLine($"Values: {string.Join(" | ", values.Select(v => v.Index))}");
//            Console.WriteLine($"Unique values = {values.Count}");
//            Console.Read();
//        }

//        static bool IsConnectedTo0(int i, int prevI)
//        {
//            var elem = input.First(inp => inp.Index == i);

//            if (elem.Associated.Contains(CompareValue))
//            {
//                return true;
//            }
//            else
//            {
//                return elem.Associated.Where(a => a != prevI).Any(c => values.Any(v => v.Index == c) || IsConnectedTo0(c, elem.Index));
//            }
//        }
//    }

//    public class InputItem
//    {
//        public int Index { get; set; }
//        public List<int> Associated { get; set; }
//    }
//}
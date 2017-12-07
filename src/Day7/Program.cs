using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day7
{
    class Program
    {
        private static List<StructureProgram> Building = new List<StructureProgram>();
        private static int AmountOfRedistributions = 0;

        static void Main(string[] args)
        {
            CreateBuilding();

            var bottomPrograms = Building.Where(b => b.Weight == Building.Min(b2 => b2.Weight));

            var programsNotInParents = Building.First(b => !ProgramIsInParent(b.Name));


            Console.WriteLine($"The bottom building is: {programsNotInParents.Name}");
        }

        private static void CreateBuilding()
        {
            foreach(var line in File.ReadAllLines("input.txt"))
            {
                Building.Add(new StructureProgram(line));
            }
        }

        private static bool ProgramIsInParent(string program)
        {
            return Building.Any(b => b.Parents.Contains(program));
        }
    }

    public class StructureProgram
    {
        public StructureProgram(string line)
        {
            Name = line.Split(' ')[0];
            Weight = int.Parse(line.Split('(')[1].Split(')')[0]);
            Parents = line.Contains(">")
                ? line.Split('>')[1].Split(',').Select(v => v.Trim()).ToList()
                : new List<string>();
        }

        public string Name { get; set; }
        public int Weight { get; set; }
        public List<string> Parents { get; set; }
    }
}
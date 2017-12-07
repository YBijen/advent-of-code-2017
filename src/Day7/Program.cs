using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day7
{
    class Program
    {
        private static List<StructureProgram> Building = new List<StructureProgram>();

        static void Main(string[] args)
        {
            CreateBuilding();

            var rootProgram = Building.First(b => !ProgramIsInParent(b.Name));

            var structure = CreateStructuredBuilding(rootProgram);

            var brokenProgram = FindBrokenStructure(structure, null);
            var weight = CalculateNewWeightForBrokenStructure(brokenProgram);
            Console.WriteLine($"The bottom building is: {rootProgram.Name}");
            Console.WriteLine($"The broken program has the name: {weight.Item3}. It's weight is {weight.Item1} and it's new weight should be: {weight.Item2}.");
        }

        private static void CreateBuilding()
        {
            foreach (var line in File.ReadAllLines("input.txt"))
            //foreach(var line in File.ReadAllLines("testInput.txt"))
            {
                Building.Add(new StructureProgram(line));
            }
        }

        private static TreeProgramItem CreateStructuredBuilding(StructureProgram program) => new TreeProgramItem()
        {
            Item = program,
            Parents = program.Parents.Select(p => Building.First(b => b.Name == p)).Select(psp => CreateStructuredBuilding(psp)).ToList()
        };

        private static bool ProgramIsInParent(string program)
        {
            return Building.Any(b => b.Parents.Contains(program));
        }

        private static TreeProgramItem FindBrokenStructure(TreeProgramItem item, TreeProgramItem parent)
        {
            var brokenParents = item.Parents.GroupBy(p => p.FullWeight).Where(g => g.Count() == 1);
            if (!brokenParents.Any())
            {
                return parent;
            }
            return FindBrokenStructure(brokenParents.First().First(), item);
        }

        /// <summary>
        /// Return a tuple with the values
        /// CurrentWeight
        /// NewWeight
        /// Broken Program name
        /// </summary>
        /// <param name="broken"></param>
        /// <returns></returns>
        private static Tuple<int, int, string> CalculateNewWeightForBrokenStructure(TreeProgramItem broken)
        {
            var groupedParentWeights = broken.Parents.GroupBy(p => p.FullWeight);
            var invalidProgram = groupedParentWeights.Where(g => g.Count() == 1).First().First();
            var invalidWeight = invalidProgram.FullWeight;
            var correctWeight = groupedParentWeights.Where(g => g.Count() > 1).First().First().FullWeight;

            var differ = correctWeight - invalidWeight;
            return Tuple.Create<int, int, string>(invalidProgram.Item.Weight, (invalidProgram.Item.Weight + differ), invalidProgram.Item.Name);
        }
    }

    public class TreeProgramItem
    {
        public StructureProgram Item { get; set; }

        public int FullWeight
        {
            get
            {
                return Parents.Sum(p => p.FullWeight) + Item.Weight;
            }
        }

        public List<TreeProgramItem> Parents { get; set; }
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
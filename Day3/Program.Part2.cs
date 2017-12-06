using System;
using System.Collections.Generic;
using System.Linq;

namespace Day3
{
    class Program
    {
        static int ASSIGNMENT_INPUT = 325489;
        static int input = 145;

        static List<Tuple<int, int>> AdjacentValues = new List<Tuple<int, int>>()
        {
            new Tuple<int, int>(-1, 1),
            new Tuple<int, int>(-1, 0),
            new Tuple<int, int>(-1, -1),
            new Tuple<int, int>(0, 1),
            new Tuple<int, int>(0, -1),
            new Tuple<int, int>(1, 1),
            new Tuple<int, int>(1, 0),
            new Tuple<int, int>(1, -1)
        };
        static List<ResultItem> result = new List<ResultItem>();

        static void Main(string[] args)
        {
            if(args != null && args.Length>  0)
            {
                int.TryParse(args[0], out input);
            }

            var movingX = 1;
            var movingY = 0;

            var currentX = 0;
            var currentY = 0;

            var segmentLength = 1;
            var segmentPassed = 0;

            // Add the starting Position to the list
            result.Add(new ResultItem(1, 0, 0));

            var currentValue = 1;

            while(currentValue < ASSIGNMENT_INPUT)
            {
                currentX += movingX;
                currentY += movingY;
                segmentPassed++;

                currentValue = SumAdjacentSquareValues(currentX, currentY);
                result.Add(new ResultItem(currentValue, currentX, currentY));

                if(segmentPassed == segmentLength)
                {
                    segmentPassed = 0;

                    // Y always gets the old value from X
                    var tempX = movingX;
                    movingX = -movingY;
                    movingY = tempX;

                    if(movingY == 0)
                    {
                        segmentLength++;
                    }
                }
            }
            Console.WriteLine($"The first value larger then our input: {input} is {currentValue}.");
        }

        public static int SumAdjacentSquareValues(int x, int y)
        {
            var sumValue = 0;
            foreach(var adjacentCoordinates in AdjacentValues)
            {
                sumValue += result.Find(r => r.X == (x + adjacentCoordinates.Item1) && r.Y == (y + adjacentCoordinates.Item2))?.Value ?? 0;
            }
            return sumValue;
        }
    }

    public class ResultItem
    {
        public ResultItem(int value, int x, int y)
        {
            X = x;
            Y = y;
            Value = value;
        }

        public int Value { get; set; }

        public int X { get; set; }
        public int Y { get; set; }

        public int DistanceTo0
        {
            get
            {
                var xDistance = 0 - X;
                if (xDistance < 0) xDistance *= -1;

                var yDistance = 0 - Y;
                if (yDistance < 0) yDistance *= -1;

                return xDistance + yDistance;
            }
        }
    }
}
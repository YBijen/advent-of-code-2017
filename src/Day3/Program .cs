//using System;
//using System.Collections.Generic;
//using System.Linq;

//namespace Day3
//{
//    class Program
//    {
//        // Result is heavily based on: https://stackoverflow.com/a/3706260

//        static int input = 25;

//        static List<ResultItem> result = new List<ResultItem>();

//        static void Main(string[] args)
//        {
//            int.TryParse(args[0], out input);

//            var movingX = 1;
//            var movingY = 0;

//            var currentX = 0;
//            var currentY = 0;

//            var segmentLength = 1;
//            var segmentPassed = 0;

//            for(int i=1; i<input; i++)
//            {
//                currentX += movingX;
//                currentY += movingY;
//                segmentPassed++;

//                result.Add(new ResultItem(i, currentX, currentY));

//                if(segmentPassed == segmentLength)
//                {
//                    segmentPassed = 0;

//                    // Y always gets the old value from X
//                    var tempX = movingX;
//                    movingX = -movingY;
//                    movingY = tempX;

//                    if(movingY == 0)
//                    {
//                        segmentLength++;
//                    }
//                }
//            }
//            Console.WriteLine($"Distance to 0 from given input {input} is: {result.Last().DistanceTo0}");
//        }
//    }

//    public class ResultItem
//    {
//        public ResultItem(int value, int x, int y)
//        {
//            X = x;
//            Y = y;
//            Value = value;
//        }

//        public int Value { get; set; }

//        public int X { get; set; }
//        public int Y { get; set; }

//        public int DistanceTo0
//        {
//            get
//            {
//                var xDistance = 0 - X;
//                if (xDistance < 0) xDistance *= -1;

//                var yDistance = 0 - Y;
//                if (yDistance < 0) yDistance *= -1;

//                return xDistance + yDistance;
//            }
//        }
//    }
//}
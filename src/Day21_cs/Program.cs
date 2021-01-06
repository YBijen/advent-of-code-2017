using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day21_cs
{
    class Program
    {
        private static readonly Dictionary<string, string> _ruleBook = new Dictionary<string, string>();

        static void Main(string[] args)
        {
            CreateRuleBook(debug: true);
        }

        private static void CreateRuleBook(bool debug)
        {
            var fileName = debug ? "inputTest.txt" : "input.txt";

            foreach(var rule in File.ReadAllLines(fileName))
            {
                var keyImage = rule.Split(" => ")[0].Replace("/", "");
                var result = rule.Split(" => ")[1].Replace("/", "");

                CreateAllOrientationsForImage(keyImage).ForEach(key => _ruleBook.Add(key, result));
            }
        }

        private static List<string> CreateAllOrientationsForImage(string image)
        {
            var imageSize = (int)Math.Sqrt(image.Length);

            var flippedImage = FlipImage(image, imageSize);

            return RotateImage360(image, imageSize)
                .Union(RotateImage360(flippedImage, imageSize))
                .Distinct()
                .ToList();
        }

        private static string FlipImage(string image, int imageSize)
        {
            var imageFlipped = "";
            for (var i = (image.Length - imageSize); i >= 0; i -= imageSize)
            {
                imageFlipped += string.Join("", image.Skip(i).Take(imageSize));
            }
            return imageFlipped;
        }

        private static IEnumerable<string> RotateImage360(string input, int imageSize)
        {
            for (var r = 0; r <= 270; r += 90)
            {
                if (r > 0)
                {
                    yield return input;
                }

                yield return RotateImage(input, imageSize, r);
            }
        }

        private static string RotateImage(string image, int imageSize, int rotation) =>
            string.Join("", Enumerable.Range(0, image.Length)
                .Select(x => image[CalcIndexForRotation(image.Length, imageSize, rotation, x % imageSize, x / imageSize)])
            );

        private static int CalcIndexForRotation(int imageLength, int imageSize, int rotation, int x, int y)
        {
            var maxIndex = imageLength - 1;
            var maxX = imageSize - 1;
            var maxY = maxIndex - maxX;

            return rotation switch
            {
                0 => y * imageSize + x,
                90 => maxY + y - (x * imageSize),
                180 => maxIndex - (y * imageSize) - x,
                270 => maxX - y + (x * imageSize),
                _ => throw new Exception("Invalid rotation value: " + rotation)
            };
        }
    }
}

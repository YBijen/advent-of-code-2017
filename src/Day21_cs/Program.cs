using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Day21_cs
{
    class Program
    {
        private const string START_IMAGE = ".#...####";
        private static readonly Dictionary<string, string> _ruleBook = new Dictionary<string, string>();

        static void Main(string[] args)
        {
            AssertLogic();
            Console.WriteLine($"Result part 1: {SolvePartOne()}");
            Console.WriteLine($"Result part 2: {SolvePartTwo()}");
        }

        private static int SolvePartOne() => PerformIterations(5).Count(c => c == '#');
        private static int SolvePartTwo() => PerformIterations(18).Count(c => c == '#');

        private static string PerformIterations(int iterations)
        {
            var image = START_IMAGE;
            for (var i = 0; i < iterations; i++)
            {
                if(i == 0) // Exception for first run
                {
                    image = ConvertImageAccordingToRuleBook(image);
                    continue;
                }

                var imageSize = (int)Math.Sqrt(image.Length);
                var subImageSize = image.Length % 2 == 0 ? 2 : 3;

                var subImages = SplitImageIntoSubImages(image, imageSize, subImageSize);
                var convertedSubImages = ConvertImageListAccordingToRuleBook(subImages);
                image = CombineSubImagesIntoImage(convertedSubImages);
            }
            return image;
        }

        private static string CombineSubImagesIntoImage(List<string> subImages)
        {
            var image = new StringBuilder();

            var subImagesPerLine = (int)Math.Sqrt(subImages.Count);
            var subImageLength = subImages[0].Length;
            var subImageSize = (int)Math.Sqrt(subImageLength);

            var newSize = subImagesPerLine * subImageSize;
            for(var y = 0; y < newSize; y++)
            {
                var subImageY = (int)(y / subImageSize);
                var yToGet = y % subImageSize;

                for (var x = 0; x < newSize; x++)
                {
                    var subImageX = (int)(x / subImageSize);

                    var subImageIndex = CalcIndexForRotation(subImages.Count, subImagesPerLine, 0, subImageX, subImageY);
                    var subImage = subImages[subImageIndex];

                    var xToGet = x % subImageSize;

                    var indexToGet = CalcIndexForRotation(subImageLength, subImageSize, 0, xToGet, yToGet);
                    image.Append(subImage[indexToGet]);
                }
            }
            return image.ToString();
        }


        private static List<string> SplitImageIntoSubImages(string image, int imageSize, int subImageSize)
        {
            var subImageLength = (int)Math.Pow(subImageSize, 2);
            var totalSubImages = (image.Length / subImageLength);
            var subImagesPerLine = (int)Math.Sqrt(totalSubImages);

            var subImages = Enumerable.Range(0, totalSubImages).Select(i => "").ToList();

            for (var y = 0; y < imageSize; y++)
            {
                var subImageY = (int)(y / subImageSize);
                var yToGet = y % subImageSize;

                for (var x = 0; x < imageSize; x++)
                {
                    var subImageX = (int)(x / subImageSize);

                    var subImageIndex = CalcIndexForRotation(totalSubImages, subImagesPerLine, 0, subImageX, subImageY);

                    var xToGet = x % subImageSize;

                    var indexToGet = CalcIndexForRotation(image.Length, imageSize, 0, x, y);
                    subImages[subImageIndex] += image[indexToGet];
                }
            }
            return subImages;
        }

        private static List<string> ConvertImageListAccordingToRuleBook(List<string> imageList) =>
            imageList.Select(ConvertImageAccordingToRuleBook).ToList();

        private static string ConvertImageAccordingToRuleBook(string image) => _ruleBook[image];

        private static void CreateRuleBook(bool debug)
        {
            // Reset the rulebook
            _ruleBook.Clear();

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

        private static void AssertLogic()
        {
            CreateRuleBook(debug: true);

            var subImageResult = SplitImageIntoSubImages("#..#........#..#", 4, 2);
            var expectedSubImageResult = new List<string> { "#...", ".#..", "..#.", "...#" };
            CollectionAssert.AreEqual(expectedSubImageResult, subImageResult);

            var convertedSubImageResult = ConvertImageListAccordingToRuleBook(subImageResult);
            var expectedConvertedSubImageResult = new List<string> { "##.#.....", "##.#.....", "##.#.....", "##.#....." };
            CollectionAssert.AreEqual(expectedConvertedSubImageResult, convertedSubImageResult);

            var combinedImageResult = CombineSubImagesIntoImage(convertedSubImageResult);
            var expectedCombinedImageResult = "##.##.#..#........##.##.#..#........";
            Assert.AreEqual(expectedCombinedImageResult, combinedImageResult);

            var resultAfterOneIteration = PerformIterations(1);
            var expectedResultAfterOneIteration = "#..#........#..#";
            Assert.AreEqual(expectedResultAfterOneIteration, resultAfterOneIteration);

            var resultAfterTwoIterations = PerformIterations(2);
            var expectedResultAfterTwoIterations = "##.##.#..#........##.##.#..#........";
            Assert.AreEqual(expectedResultAfterTwoIterations, resultAfterTwoIterations);

            CreateRuleBook(debug: false);

            Assert.AreEqual(158, SolvePartOne());
            Assert.AreEqual(2301762, SolvePartTwo());
        }
    }
}

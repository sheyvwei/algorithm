using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BubbleSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] sourceArray = new int[] { 1, 3, 5, 6,2,4 ,76,56};
            int[] resultArray = sort(sourceArray);
            for(int i = 0;i<= resultArray.Length-1; i++)
            {
                Console.WriteLine(resultArray[i]);

            }
            Console.ReadKey();
        }
        /// <summary>
        /// 冒泡排序
        /// </summary>
        /// <param name="sourceArray"></param>
        /// <returns></returns>
        public static int []  sort(int[] sourceArray)
        {
            int[] arr  = new int [sourceArray.Length];
            Array.Copy(sourceArray, arr,  sourceArray.Length);//复制出来
            //两个相邻数字比较，循环i-1次
            for(int i = 1; i < arr.Length -1; i++)
            {
                
                bool flag = true;//标记，如果没有替换就没必要进行下次循环了

                for (int j = 0; j < arr.Length - i; j++)
                {
                    if(arr[j] > arr[j + 1])
                    {
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                        flag = false;
                    }
                }
                if (flag)
                    break;
            }
            return arr;
        }
    }
}

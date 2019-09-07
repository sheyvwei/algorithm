
public class Solution {
    // 嵌套for循环，O(n的平方)
    public int maxProfit(int[] prices){
        int len = prices.length;
        int count = 0;
        for(int i = 0; i < len; i++) {
            for (int j = i; j<len; j++) {
                count = Math.max(prices[j]-prices[i],count);
            }
        }
        return count;
    }
    public static void main(String[] args) {
        Test t = new Test();
        int [] prices = new int[] { 1,2};
        int result = t.maxProfit(prices);
        System.out.println(result);
    }
}
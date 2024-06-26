/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1;
        int right = n;
        while (true) {
            int middle = (right - left)/2 + left;
            int num = guess(middle);
            if (num == 0) {
                return middle;
            }
            else if (num == 1) {
                left = middle + 1;
            }
            else {
                right = middle - 1;
            }
        }
    }
}

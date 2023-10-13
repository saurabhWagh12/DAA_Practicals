import java.util.ArrayList;
import java.util.List;

public class PalindromeF{
    public static List<String> findAllSubsequences(String str) {
        List<String> subsequences = new ArrayList<>();
        Subsequences(str, "", 0, subsequences);
        return subsequences;
    }

    private static void Subsequences(String str, String current, int index, List<String> subsequences) {
        if (index == str.length()) {
            subsequences.add(current);
            return;
        }

        Subsequences(str, current + str.charAt(index), index + 1, subsequences);
        Subsequences(str, current, index + 1, subsequences);
    }

    public static boolean isPalindrome(String str) {
        int i = 0;
        int j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        String input = "ACGTGTCAAAATCG";
        List<String> subsequences = findAllSubsequences(input);
        int count = Integer.MIN_VALUE;
        int countp = 0;
        for (String subsequence : subsequences) {
            if (isPalindrome(subsequence)) {
                System.out.println(subsequence);
                count = Math.max(count,subsequence.length());
                countp++;
            }
        }
        System.out.println("Max-length: "+count);

    }
}

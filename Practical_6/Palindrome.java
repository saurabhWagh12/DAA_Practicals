import java.util.ArrayList;
import java.util.List;

public class Palindrome{

    private static boolean checkPalindrome(String s){
        for(int i=0;i<s.length()/2;i++){
            if(s.charAt(i)!=s.charAt(s.length()-i-1)){
                return false;
            }
        }
        return true;
    }

    public static int findPalindrome(String s){
        int count=0;
        int maxLen = Integer.MIN_VALUE;
        for(int i=0;i<s.length();i++){
            for(int j=i+1;j<s.length();j++){
                String st = s.substring(i, j+1);
                count++;
                boolean isPalindrome = checkPalindrome(st);
                if(isPalindrome){
                    maxLen = Math.max(maxLen, st.length());
                    System.out.println(st);
                }
            }
        }
        System.out.println("\nMaximum Length: "+maxLen);
        return count;
    } 

    public static void main(String args[]){
        int count = findPalindrome("ACGTGTCAAAATCG");
        System.out.println(count);
        
    }
}
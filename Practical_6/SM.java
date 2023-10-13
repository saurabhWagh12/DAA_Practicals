public class SM {

    static class block{
        int val;
        char dir;
        public block(int v,char d){
            val = v;
            dir = d;
        }
    }

    private static void find(block b,block matrix[][],String s1,int i,int j,StringBuilder sb){
        if(b.dir=='H'){
            return;
        }

        if(b.dir=='D'){
                sb.append(s1.charAt(i-1));
                i = i-1; j = j-1;
                b = matrix[i][j];
                find(b, matrix, s1, i, j, sb);
            }else if(b.dir=='S'){
                j = j-1;
                b = matrix[i][j];
                find(b, matrix, s1, i, j, sb);
            }else{
                i = i-1;
                b = matrix[i][j];
                find(b, matrix, s1, i, j, sb);
            }

    }

    private static void findSubsequence(String s1,String s2,block matrix[][],StringBuilder sb){
        int rows = s1.length()+1;
        int cols = s2.length()+1;
        int i=rows-1,j=cols-1;
        block b = matrix[rows-1][cols-1];
        find(b, matrix, s1, i, j, sb);
        
    }

    public static void longestCommonSubsequence(String s1, String s2) {
        block matrix[][] = new block[s1.length()+1][s2.length()+1];
        int rows = s1.length()+1;
        int cols = s2.length()+1;

        for(int i=0;i<rows;i++){
            matrix[i][0] = new block(0,'H');
        }

        for(int i=0;i<cols;i++){
            matrix[0][i] = new block(0,'H');
        }

        for(int i=1;i<rows;i++){
            for(int j=1;j<cols;j++){
                //Equal
                if(s1.charAt(i-1)==s2.charAt(j-1)){
                    matrix[i][j] = new block(matrix[i-1][j-1].val+1,'D');
                }else{
                    //Not Equal
                    if(matrix[i-1][j].val>=matrix[i][j-1].val){
                        matrix[i][j] = new block(matrix[i-1][j].val,'U');
                    }else{
                        matrix[i][j] = new block(matrix[i][j-1].val,'S');
                    }
                }
            }
        }


        

        System.out.println();
        StringBuilder sb = new StringBuilder("");
        findSubsequence(s1,s2,matrix,sb);
        int i,j;
        System.out.println("\n"+sb.reverse().toString()+"\tLength of String: "+sb.length()+"\n");

        //Printing Matrix
        for (i = 1; i < rows; i++) {
            for (j = 1; j < cols; j++) {
                System.out.print(matrix[i][j].val + "/" + matrix[i][j].dir + "\t");
            }
            System.out.println();
        }

    }

    public static void main(String args[]) {
        
        String A = "AGCCCTAAGGGCTACCTAGCTT";
        String B = "GACAGCCTACAAGCGTTAGCTTG";
        longestCommonSubsequence(A,B);
    }
}

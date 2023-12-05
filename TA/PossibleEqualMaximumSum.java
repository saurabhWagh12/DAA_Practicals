import java.util.*;
public class PossibleEqualMaximumSum{
    private Stack<Integer> s1,s2,s3;
    int n;
    
    public PossibleEqualMaximumSum(int n){
        s1 = new Stack<>();
        s2 = new Stack<>();
        s3 = new Stack<>();
        this.n = n;
    }

    public int addInStack(int i, int num) {
        switch (i) {
            case 1:
                if(s1.size()<this.n)
                    s1.push(num);
                return s1.peek();
            case 2:
                if(s2.size()<this.n)
                    s2.push(num);
                return s2.peek();
            case 3:
                if(s3.size()<this.n)
                    s3.push(num);
                return s3.peek();
            default:
                return -1;
        }
    }
    

    private int findParticularSum(Stack<Integer> s){
        int sum=0;
        for (Integer element : s) {
            sum += element;
        }
        return sum;
    }

    private int checker(int m1,int m2,int m3){
        int m = Math.max(m1,Math.max(m2,m3));
        if(m1==m2 && m2==m3){
            return 0;
        }
        if(m==m1){
            return 1;
        }else if(m==m2){
            return 2;
        }else if(m==m3){
            return 3;
        } 

        return -1;
    }

    private int findMaxSum(){
         
        int m1=this.findParticularSum(s1);
        int m2=this.findParticularSum(s2);
        int m3=this.findParticularSum(s3);

        return checker(m1, m2, m3);
    }

    private void removeFromStack(){
        int i = this.findMaxSum();
        if(i==0){
            int m=0;
            for (Integer element : s3) {
                m += element;
            }
            System.out.println("Maximum Sum: "+m);
            return;
        }else if(s1.isEmpty() || s3.isEmpty() || s2.isEmpty()){
            System.out.println("Not Possible!!!");
            return;
        }

        if(i==1){
            s1.pop();
        }else if(i==2){
            s2.pop();
        }else if(i==3){
            s3.pop();
        }

        removeFromStack();
    }

    public void findAns(){
        this.removeFromStack();
        System.out.print("\n"+"Stack 1:\t");
        int m = s1.size();
        for(int i=m-1;i>=0;i--){
            System.out.print(s1.pop()+"\t");
        }
        System.out.print("\n"+"Stack 2:\t");
        m = s2.size();
        for(int i=m-1;i>=0;i--){
            System.out.print(s2.pop()+"\t");
        }
        System.out.print("\n"+"Stack 3:\t");
        m = s3.size();
        for(int i=m-1;i>=0;i--){
            System.out.print(s3.pop()+"\t");
        }
    }

}
import java.util.ArrayList;

public class SumofSubsets {
    private static int sum(ArrayList<Integer> list){
        int sum=0;
        for(Integer i:list){
            sum+=i;
        }
        return sum;
    }
    private static void find(int arr[],int i,int sum,ArrayList<Integer> list){
        if(i==arr.length ){
            if(sum(list)==sum)
                System.out.println("Last: "+list);
            return;
        }
        if(sum(list)==sum){
            System.out.println("Middle: "+list);
            return;
        }
        if(sum(list)>sum){
            System.out.println("Exceeded: "+list);
            return;
        }
        
        //Dont Add
        find(arr, i+1, sum, list);
        //Add
        list.add(arr[i]);
        find(arr,i+1,sum,list);
        list.remove(list.size()-1);
    }
    public static void main(String[] args) {
        int arr[] = {5,10,12,13,15,18};
        find(arr,0,30,new ArrayList<>());
    }
}
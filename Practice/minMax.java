public class minMax {
    static int fmin=Integer.MAX_VALUE,fmax=Integer.MIN_VALUE,min=Integer.MAX_VALUE,min1=Integer.MAX_VALUE,max=Integer.MIN_VALUE,max1=Integer.MIN_VALUE;
    public static void findMinMax(int arr[],int l,int h){
        if(l==h){
            min = arr[l];
            max = arr[l];
            return;
        }
        if(l==h-1){
            max = Math.max(arr[l],arr[h]);
            min = Math.min(arr[l],arr[h]);
            return;
        }
            int mid = l+(h-l)/2;
            findMinMax(arr, l, mid-1);
            findMinMax(arr, mid+1, h);
            fmin = Math.min(Math.min(min,min1),fmin);
            fmax = Math.max(Math.max(max,max1),fmax);

    }
    public static void main(String args[]){
        int arr[] = {-10,70,12,-50,60,32,45,95,-19};
        findMinMax(arr,0,8);
        System.out.println(fmin+" "+fmax);
    }
    
}

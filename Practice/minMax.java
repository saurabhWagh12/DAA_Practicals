public class minMax {
    static int[] findMinMax(int arr[],int l,int h){
        if(l==h){
            int f[] = {arr[l],arr[l]};

            return f;
        }else if(h-l==1){
            int f[] = {Math.max(arr[h],arr[l]),Math.min(arr[h],arr[l])};
            return f;
        }

        int mid = l+(h-l)/2;
        int f1[] = findMinMax(arr, l, mid);
        int f2[] = findMinMax(arr, mid+1, h);
        System.out.println("f1: "+f1[0]+" "+f1[1]);
        System.out.println("f2: "+f2[0]+" "+f2[1]);


        int fm[] = new int[2];
        fm[1] = Math.min(f1[1],f2[1]);
        fm[0] = Math.max(f1[0],f2[0]);
        return fm;
    }
    public static void main(String args[]){
        int arr[] = {-10,70,12,50,60,32,-45,9,19};
        int f[] = findMinMax(arr,0,8);
        System.out.println(f[1]+" "+f[0]);
    }
    
}

import java.util.Arrays;

public class Prims{

    private static void findMST(int graph[][],int key[],boolean mst[],int parent[]){
        int i=0;
        int len = key.length;
        while(i<len){
            int mini = Integer.MAX_VALUE;
            int idx = -1;
            for(int j=0;j<len;j++){
                if(mst[j]==false && mini>key[j]){
                    mini = key[j];
                    idx = j;
                }
            }
            mst[idx]=true;
            for (int k = 0; k < len; k++) {
                if (!mst[k] && graph[idx][k] != 0 && graph[idx][k] < key[k]) {
                    key[k] = graph[idx][k];
                    parent[k] = idx;
                }
            }
            i++;
        }
    }

    public static void main(String args[]){
        int graph[][] = {
            {0,2,0,6,0},
            {2,0,3,8,5},
            {0,3,0,0,7},
            {6,8,0,0,0},
            {0,5,7,0,0}
        };
        boolean mst[] = new boolean[5];
        int parent[] = new int[5];
        int key[] = new int[5];
        Arrays.fill(mst,false);
        Arrays.fill(key,Integer.MAX_VALUE);
        key[0] = 0;
        Arrays.fill(parent,-1);

        findMST(graph,key,mst,parent);

        for(int i=1;i<parent.length;i++){
            System.out.println(i+"->"+parent[i]+": "+graph[i][parent[i]]);
        }

    }
}
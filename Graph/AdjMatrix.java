package Graph;

public class AdjMatrix implements Graph {
    private double m[][];
    public AdjMatrix(int n){
        m=new double[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j) m[i][j]=0;
                else m[i][j]=Double.POSITIVE_INFINITY;
            }
        }
    }

    public void addEdge(int u, int v, double w){
        if(w<=0) return;
        if(u<m.length && v<m.length){
            m[u][v]=w;
        }
    }
    public String toString(){
        String s="";
        for(int i=0; i<m.length; i++){
            for(int j=0;j<m.length; j++){
                s+=m[i][j]+" ";
            }
            s+="\n";
        }
        return s;
    }
}

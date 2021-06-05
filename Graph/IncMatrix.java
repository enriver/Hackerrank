package Graph;

public class IncMatrix implements Graph {
    private double m[][];
    private int cur=0;
    public IncMatrix(int v, int e){
        m=new double[v][e];
    }

    public void addEdge(int u, int v, double w){
        m[u][cur]=-w;
        m[v][cur]=w;
        cur++;
    }
    public String toString(){
        String s="";
        for(int i=0; i<m.length; i++){
            for(int j=0; j<cur; j++){
                s+=m[i][j]+"\t";
            }
            s+="\n";
        }
        return s;
    }
}

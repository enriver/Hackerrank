package Graph;

public class AdjList implements Graph {
    Edge[] m;

    public AdjList(int num){
        m=new Edge[num];
    }
    public void addEdge(int u, int v, double w){
        m[u]=new Edge(u,v,w,m[u]);
    }
    public String toString(){
        String result="";
        for(int i=0; i<m.length;i++){
            result+="\n["+i+"]; ";
            Edge p=m[i];
            while(p!=null){
                result+=p.getHead()+"("+p.getWeight()+")";
                p=p.n;
            }
        }
        return result;
    }
}
